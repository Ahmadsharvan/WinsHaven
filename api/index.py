#!/usr/bin/env python3
"""
Vercel serverless function entry point for WinsHaven Flask app
"""
import sys
import os

# Setup paths
api_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(api_dir)

# Add project to Python path
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

# Change working directory to project root
os.chdir(project_dir)

# Create data directory for tickets and bookings
data_dir = os.path.join(project_dir, "data")
os.makedirs(data_dir, exist_ok=True)

# Import and configure Flask app
try:
    from app import app
    print("[✓] Successfully loaded Flask app from app.py")
except Exception as e:
    print(f"[✗] Error loading app: {str(e)}")
    import traceback
    traceback.print_exc()
    
    # Create minimal fallback app
    from flask import Flask, jsonify
    app = Flask(__name__)
    
    @app.route('/')
    def error_page():
        return jsonify({"error": f"Failed to load app: {str(e)}"}), 500

# Export app for Vercel
if __name__ == "__main__":
    app.run(debug=False)
