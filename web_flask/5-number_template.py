#!/usr/bin/python3
"""Starts a Flask web application to display some messages
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays a simple message."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays a simple message."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays "C" followed by the value of the text variable.
    Replaces any underscores in the variable with a space.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' followed by the value of <text>
    variable.
    Replaces any underscores in <text> with spaces.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays "<n> is a number" only if n is an integer.
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Render a template with the given number.
    """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
