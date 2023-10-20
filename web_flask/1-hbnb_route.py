#!/usr/bin/python3
"""
script that starts a Flask web application
Route "/" displays "Hello HBNB!"
Route "/hbnb" displays "HBNB"
"""
from flask import Flask
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


"""listening on 0.0.0.0 and port 5000"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
