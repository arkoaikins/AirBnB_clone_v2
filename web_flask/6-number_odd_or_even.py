#!/usr/bin/python3
"""
script that starts a Flask web application
Route "/" displays "Hello HBNB!"
Route "/hbnb" displays "HBNB"
Route "/c/<text>":displays "C" followed by the value of the text variable
Route "/python/<text>":displays "python" followed by the value of the text
Route "/number_template/<n>":display HTML page only if n is an integer
Route "/number_odd_even/<n>":display a HTML page only if n is an integer
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def web_app():
    """
    the home route which displays Hello HBNB!
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def web_hbnb():
    """
    hbnb route to return HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def web_text(text):
    return "C " + text.replace("_", " ")


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def web_python(text="is cool"):
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def web_number(n):
    """display if only n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def web_templates(n):
    """display HTML tage if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def web_odd(n):
    """displays HTML page only if n is an integer"""
    return render_template("6-number_odd_or_even.html", n=n)


"""listening on 0.0.0.0 and port 5000"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
