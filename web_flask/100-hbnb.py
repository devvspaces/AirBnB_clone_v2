#!/usr/bin/python3
"""Starts a Flask web application.
Renders a HTML page with a list of all State and City
objects in DBStorage.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Renders HBnB HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(exc):
    """Kill the current DB session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
