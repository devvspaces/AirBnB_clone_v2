#!/usr/bin/python3
"""
Execute a Minimal Flask application
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Renders a simple string in the route /"""
    return "Hello HBNB!"


if __name__ == "__main__":
    """Main block
    """
    app.run(host="0.0.0.0")
