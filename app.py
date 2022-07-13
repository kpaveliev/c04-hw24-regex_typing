import os

from marshmallow.exceptions import ValidationError
from flask import Flask, request, abort

from resources import utils
from resources.commands import CommandsSchema, Commands
from resources.constants import DATA_DIR, COMMANDS

app = Flask(__name__)


@app.route("/perform_query/", methods=['GET', 'POST'])
def perform_query():

    try:
        # Get data
        commands: Commands = CommandsSchema().load(request.args)
        file_path: str = os.path.join(DATA_DIR, commands.file_name)

        # Perform checks
        if commands.cmd1 not in COMMANDS or commands.cmd2 not in COMMANDS:
            raise ValueError('Wrong function passed')

        if not os.path.exists(file_path):
            raise FileNotFoundError('Wrong filename passed')

        # Perform commands passed and return results in a response
        with open(file_path, 'r') as file:
            first_result = getattr(utils, commands.cmd1 + '_')(file, commands.value1)
            second_result = getattr(utils, commands.cmd2 + '_')(first_result, commands.value2)
            return app.response_class('\n'.join([line.strip() for line in second_result]), content_type="text/plain")

    except (ValueError, FileNotFoundError, TypeError, IndexError, ValidationError) as e:
        abort(400, e)


if __name__ == '__main__':
    app.run(debug=True)
