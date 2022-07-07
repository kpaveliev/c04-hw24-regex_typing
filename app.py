import os

from flask import Flask, request, abort

import utils
from constants import DATA_DIR

app = Flask(__name__)


@app.route("/perform_query/", methods=['POST'])
def perform_query():
    # Get filename and commands from request
    file_name = request.json.get('file_name')
    cmd1 = request.json.get('cmd1') + '_'
    value1 = request.json.get('value1')
    cmd2 = request.json.get('cmd2') + '_'
    value2 = request.json.get('value2')

    # Check data passed and file path
    if None in (file_name, cmd1, value1, cmd2, value2):
        return abort(400, 'Wrong data passed')

    file_path = os.path.join(DATA_DIR, file_name)

    if not os.path.exists(file_path):
        return abort(400, 'No file found')

    # Get data from the file and perform commands
    file_data = open(file_path, 'r')
    first_result = getattr(utils, cmd1)(file_data, value1)
    second_result = getattr(utils, cmd2)(first_result, value2)

    return app.response_class(list(second_result), content_type="text/plain")


if __name__ == '__main__':
    app.run()