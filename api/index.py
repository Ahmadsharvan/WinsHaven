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
except Exception as e:
    print(f"Warning: Could not create data directory: {e}")

# Change working directory to parent for relative imports
os.chdir(parent_dir)

# Import Flask app from parent directory
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

# Export app at module level for Vercel to find it
__all__ = ['app']
