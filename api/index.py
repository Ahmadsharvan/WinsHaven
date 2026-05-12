import sys
import os
from werkzeug.middleware.proxy_fix import ProxyFix

# Set up path - go up one level to parent directory
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

# Create data directory if it doesn't exist
try:
    data_dir = os.path.join(parent_dir, "data")
    os.makedirs(data_dir, exist_ok=True)
except:
    pass

# Change working directory to parent for relative imports
original_cwd = os.getcwd()
os.chdir(parent_dir)

try:
    # Import the Flask app from app.py (one level up)
    from app import app
    
    # Apply proxy fix for Vercel headers
    app.wsgi_app = ProxyFix(
        app.wsgi_app,
        x_for=1,
        x_proto=1,
        x_host=1,
        x_port=1,
        x_prefix=1
    )
    
    print("✓ Flask app loaded successfully")
    
except Exception as e:
    print(f"✗ Error loading app: {str(e)}")
    import traceback
    traceback.print_exc()
    
    # Fallback error app
    from flask import Flask
    app = Flask(__name__)
    
    @app.route('/')
    def error():
        return f"""
        <h1>Error Loading WinsHaven</h1>
        <p>{str(e)}</p>
        <pre>{traceback.format_exc()}</pre>
        """, 500

# Export WSGI app for Vercel
# This is what Vercel's Python runtime looks for
