from flask import Flask, request, jsonify

app = Flask(__name__)

todos: list[dict] = [
    {"label": "finish react projects", "done": False},
    {"label": "walk the dog", "done": False},
    {"label": "clean my room", "done": False},
]


@app.route("/todos")
def get_todos():
    json_response = jsonify(todos)
    return json_response


@app.route("/todos", methods=["POST"])
def add_todo():

    return "Todo was added!"


@app.route("/todos/<int:position>", methods=["DELETE"])
def delete_todo(position):
    return f"Todo to delete is: {position}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3245, debug=True)
