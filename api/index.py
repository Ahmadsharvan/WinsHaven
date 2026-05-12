import sys
import os

# Ensure we're in the right directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add parent to path
sys.path.insert(0, parent_dir)

# Set working directory
os.chdir(parent_dir)

# Create data directory
data_dir = os.path.join(parent_dir, "data")
os.makedirs(data_dir, exist_ok=True)

# Now import app
try:
    from app import app
    print("✓ App imported successfully from parent directory")
except ImportError as e:
    print(f"✗ Failed to import app: {e}")
    import traceback
    traceback.print_exc()
    
    # Fallback minimal app
    from flask import Flask
    app = Flask(__name__)
    
    @app.route('/')
    def error():
        return f"""
        <h1>⚠️ Error Loading WinsHaven</h1>
        <p>Failed to import Flask app</p>
        <pre>{str(e)}</pre>
        """, 500

# Vercel requires these functions for proper WSGI handling
def handler(request):
    """Handle Vercel requests"""
    return app(request.environ, request.start_response)

# Also export app directly for Vercel's Python runtime
if __name__ != "__main__":
    # Make sure app is accessible at module level for Vercel
    pass

