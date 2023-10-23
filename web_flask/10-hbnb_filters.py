#!/usr/bin/python3
"""Starts a Flask web application.
Renders a HTML page with a list of all State and City
objects in DBStorage.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Renders HBnB filters HTML page with a list of all States and Amenities.
    States are sorted by name.
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """Kill the current DB session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
