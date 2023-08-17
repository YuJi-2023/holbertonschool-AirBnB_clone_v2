#!/usr/bin/python3
"""start a flask web app"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def states():
    """display a filter html page"""
    return render_template("10-hbnb_filters.html")


@app.teardown_appcontext
def remove_session(exception):
    """remove current SQLAlchemy Session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
