#!/usr/bin/python3
"""script that starts a Flask web applic"""
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """display a HTML page"""
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    states = storage.all("State")
    return render_template("100-hbnb.html",
                           amenities=amenities,
                           places=places,
                           states=states)


@app.teardown_appcontext
def teardown(exc=None):
    """close storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
