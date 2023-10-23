#!/usr/bin/python3
"""Starts a Flask web application.
Renders a HTML page with a list of all State and City
objects in DBStorage.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Renders an HTML page with a list of all States.
    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Renders an HTML page with info about <id>, if found."""
    for obj in storage.all("State").values():
        if obj.id == id:
            return render_template("9-states.html", state=obj)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Kill the current DB session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
