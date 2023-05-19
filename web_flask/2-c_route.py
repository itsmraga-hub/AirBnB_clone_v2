#!/usr/bin/python3
"""
    Write a script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ” followed by the value of the text variable
            (replace underscore _ symbols with a space )
"""


from flask import Flask
# from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
        Routes:
            /: display “Hello HBNB!”
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
        Routes:
            /: display “Hello HBNB!”
            /hbnb: display “HBNB”
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
        Routes:
            /: display “Hello HBNB!”
            /hbnb: display “HBNB”
            /c/<text>
    """
    text = text.replace("_", " ")
    return 'C {}'.format(text)


# Start the Flask application
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
