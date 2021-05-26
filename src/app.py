import json
from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

# Endpoint: GET /todos
#
# @app.route('/todos', methods=['GET'])
# def hello_world():
#     return "<h1>Hello!</h1>"
#
@app.route('/todos', methods=['GET'])
def hello_world():
        json_text = jsonify(todos)
        print("Array Todos: ", todos)
        return json_text

# Endpoint: POST /todos
#
# @app.route('/todos', methods=['POST'])
# def add_new_todo():
#     request_body = request.data
#     print("Incoming request with the following body", request_body)
#     return 'Response for the POST todo'
#
# {"label":"My third task","done":false}
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    json_data = jsonify(todos)
    print("New Array Todos: ", todos)
    return json_data

# Endpoint: DELETE /todos/<int:position>
#
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    for i in range(len(todos)):
        if i == position:
            del todos[i]
    json_data = jsonify(todos)
    print("This is the position to delete: ",position)
    print("New Array Todos: ", todos)
    return json_data
 
# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)