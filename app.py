from flask import Flask, request, abort

import utils

app = Flask(__name__)


@app.route("/perform_query/", methods=['GET', 'POST'])
def perform_query():
    # Extract commands from request and check them
    file_path, cmd1, value1, cmd2, value2 = utils.get_args(request.args)

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