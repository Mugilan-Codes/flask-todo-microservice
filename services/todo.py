import json
import os

from flask import Flask, jsonify, make_response

app = Flask(__name__)

database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

with open(f"{database_path}/database/todos.json", "r") as jsf:
    todo_list = json.load(jsf)


@app.route("/", methods=["GET"])
def hello():
    """Greet the User"""

    return "Todo service is up"


if __name__ == "__main__":
    app.run(port=5001, debug=True)
