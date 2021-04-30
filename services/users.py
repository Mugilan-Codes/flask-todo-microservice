from flask import Flask, jsonify, make_response
import requests
import os
import simplejson as json

app = Flask(__name__)

database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(database_path)

with open(f"{database_path}/database/users.json", "r") as f:
    usr = json.load(f)


@app.route("/", methods=["GET"])
def hello():
    """Greet the User"""

    return "Hey! The service is up, how about doing something useful"


if __name__ == "__main__":
    app.run(port=5000, debug=True)
