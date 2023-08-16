#!/usr/bin/python3
"""start a flask web app"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """display html page state list"""
    states = storage.all(State)
    #for state in states.values():
    #    state_list.append(state)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def remove_session(exception):
    """remove current SQLAlchemy Session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
