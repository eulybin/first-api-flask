from flask import Flask, request

app = Flask(__name__)


@app.route("/todos")
def getTodos():
    return "Here is a list of all todos."


@app.route("/todos/addTodo", methods=["POST"])
def addTodo():
    return "Todo was added!"


@app.route("/todos/deleteTodo/<position>", methods=["DELETE"])
def deleteTodo(position):
    return "Todo to delete is: " + position


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3245, debug=True)
