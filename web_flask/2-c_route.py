#!/usr/bin/python3
""" script that starts a Flask web applica"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def HBNB():
    """PRINT HELLO HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """PRINT HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """display C  followed by the value of the text var"""
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
