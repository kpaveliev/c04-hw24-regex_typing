import os

from flask import Flask, request, abort

import utils
from constants import DATA_DIR, COMMANDS

app = Flask(__name__)


@app.route("/perform_query/", methods=['GET', 'POST'])
def perform_query():
    # Get filename and commands from request
    file_name = request.json.get('file_name')
    cmd1 = request.json.get('cmd1') + '_'
    value1 = request.json.get('value1')
    cmd2 = request.json.get('cmd2') + '_'
    value2 = request.json.get('value2')

    # Check data passed is correct and file path exists
    if (
        None in (file_name, cmd1, value1, cmd2, value2)
        or cmd1 not in COMMANDS
        or cmd2 not in COMMANDS
    ):
        return abort(400, 'Wrong params passed')

    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        return abort(400, 'Wrong filename passed')

    # Perform commands
    try:
        with open(file_path, 'r') as file:
            first_result = getattr(utils, cmd1)(file, value1)
            second_result = getattr(utils, cmd2)(first_result, value2)
    except (ValueError, TypeError) as e:
        abort(400, e)

    return app.response_class(second_result, content_type="text/plain")


if __name__ == '__main__':
    app.run(debug=True)