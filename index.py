import sys
import os

parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent)

os.makedirs(os.path.join(parent, "data"), exist_ok=True)

try:
    from app import app
except Exception as e:
    from flask import Flask
    app = Flask(__name__)
    @app.route('/')
    def err():
        return str(e), 500
