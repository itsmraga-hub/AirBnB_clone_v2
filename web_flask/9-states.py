#!/usr/bin/python3
"""
    Starts a Flask web application and fetches states from the database
"""

from flask import Flask, render_template
from models import storage

from models.state import State


app = Flask(__name__)

@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """
        /states: display a HTML page: (inside the tag BODY)
        H1 tag: “States”
        UL tag: with the list of all State objects
        present in DBStorage sorted by name (A->Z) tip
        LI tag: description of one State: <state.id>: <B><state.name></B>
        /states/<id>: display a HTML page: (inside the tag BODY)
        If a State object is found with this id:
            H1 tag: “State: ”
            H3 tag: “Cities:”
        UL tag: with the list of City objects linked to the
        State sorted by name (A->Z)
        LI tag: description of one City: <city.id>: <B><city.name></B>
        Otherwise:
            H1 tag: “Not found!”
    """
    states = storage.all(State).values()
    if id is not None:
        for state in states:
            if state.id == id:
                return render_template('9-states.html', states=state)
        return render_template('9-states.html')
    return render_template('9-states.html', states=states, full=True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
