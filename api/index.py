import sys
import os

# Set up path
parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent)

# Create data directory
try:
    data_dir = os.path.join(parent, "data")
    os.makedirs(data_dir, exist_ok=True)
except:
    pass

try:
    from app import app
except Exception as e:
    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def error():
        return f"Error: {str(e)}", 500


