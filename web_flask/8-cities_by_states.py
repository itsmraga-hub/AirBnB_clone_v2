#!/usr/bin/python3
"""
    Starts a Flask web application and fetches states from the database
"""

from flask import Flask, render_template
from models import storage

from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    """
        Remove current SQLAlchemy Session after each request
    """
    storage.close()

@app.route('/cities_by_state', strict_slashes=False)
def cities_by_state():
    """
        H1 tag: “States”
        UL tag: with the list of all State objects present in
        DBStorage sorted by name (A->Z)
    """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
