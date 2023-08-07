from flask import Flask
from flask.json import jsonify
from redis import Redis

app = Flask(__name__)
redis_db = Redis("localhost", 6379, 0)
DEFAULT_QUEUE = "default"


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/events", methods=["GET"])
def get_events():
    result = redis_db.lrange(DEFAULT_QUEUE, 0, -1)
    result = [i.decode() for i in result]
    return jsonify({"result": result})


@app.route("/events/<task_name>/", methods=["GET"])
def add_event(task_name):
    result = redis_db.lpush(DEFAULT_QUEUE, task_name)
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run()
