#!/usr/bin/python3
"""
    Starts a Flask web application and fetches states from the database
"""

from flask import Flask, render_template
from models import storage

from models.state import State


app = Flask(__name__)


@app.route('/states-list', strict_slashes=False)
def states_list():
    """
        Display a page with all states in database listed
    """
    states = sorted(list(storage.all("State").values()))
    return render_template('7-states_list.html'), states=states)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
