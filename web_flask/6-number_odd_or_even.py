#!/usr/bin/python3
"""start a flask web app"""
from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """first route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """second route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """c variable route"""
    new_text = text.replace("_", " ")
    return f"C {escape(new_text)}"


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python_route(text="is cool"):
    """python variable route"""
    new_text = text.replace("_", " ")
    return f"Python {escape(new_text)}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """number route"""
    return f"{n} is a number"


@app.route("/number_template/", strict_slashes=False)
@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n=None):
    """generate template of html page"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/", strict_slashes=False)
@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n=None):
    """generate template of html page"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
