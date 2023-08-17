#!/usr/bin/python3
"""start a flask web app"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """display html page of state list"""
    state_list = storage.all(State)
    return render_template("7-states_list.html", state_list=state_list)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id=None):
    """display html page of state with given id and its city list"""
    state_list = storage.all(State)
    city_list = storage.all(City)

    state_found = None
    for s in state_list.values():
        if s.id == id:
            state_found = s
            break
    if state_found:
        return render_template("9-states.html", state_found_id=id,
                               city_list=city_list, state_found=state_found)
    else:
        return render_template("9-states.html", state_found_id=None,
                               city_list=city_list, state_found=None)


@app.teardown_appcontext
def remove_session(exception):
    """remove current SQLAlchemy Session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
