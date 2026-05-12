import sys
import os
from werkzeug.middleware.proxy_fix import ProxyFix

# Set up path
parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent)

# Create data directory
try:
    data_dir = os.path.join(parent, "data")
    os.makedirs(data_dir, exist_ok=True)
except:
    pass

# Change to correct directory for relative imports
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Import the Flask app
from app import app

# Apply proxy middleware
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1, x_prefix=1)

# Export for Vercel
__all__ = ['app']
