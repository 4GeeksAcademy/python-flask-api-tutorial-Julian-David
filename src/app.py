from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
   {"label": "My first task", "done": False},
   {"label": "My second task", "done": False}
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text= jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
   request_body = request.json
   print("Incoming request with the folllowing body", request_body)
   todos.append(request_body)
   return jsonify(todos)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
   if position < 0 or position >= len(todos):
      return jsonify({"error": "Posición no válida"}), 404
   delete_todos = todos.pop(position)
   return jsonify(todos), 200


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
