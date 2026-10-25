from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman

app = Flask(__name__)

# Configure Cross-Origin Resource Sharing
CORS(app)

# Enable security headers
Talisman(
    app,
    content_security_policy=None,
    force_https=False
)
