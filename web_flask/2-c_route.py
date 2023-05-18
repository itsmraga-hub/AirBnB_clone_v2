#!/usr/bin/python3
"""
    A script that starts a Flask web application
"""


from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return f'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    text = text.replace("_", " ")
    return f'C {escape(text)}'
    

# Start the Flask application
if __name__ == '__main__':
    app.run()
