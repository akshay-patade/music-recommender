from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Import routes after initializing app to avoid circular imports
from app import routes
