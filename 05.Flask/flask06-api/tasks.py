from flask import Flask, request, jsonify

app = Flask(__name__)

# 建立一個名為 `tasks` 的資料表，用來儲存待辦事項
tasks = [
    {
        'task': 'Python程式設計備課'
    }
]


@app.route('/', methods=['GET'])
def helloworld():
    # 回傳目前資料表中的所有待辦事項
    return "<h1>Hello World</h1>"

@app.route('/tasks', methods=['GET'])
def list_tasks():
    # 回傳目前資料表中的所有待辦事項
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    # 取得使用者傳送的待辦事項
    task = request.json
    tasks.append(task)
    return jsonify(tasks), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    # 取得使用者傳送的更新資料
    task = request.json

    # 檢查待辦事項是否存在
    if task_id < 0 or task_id >= len(tasks):
        return jsonify({'message': 'task not found'}), 404

    # 更新待辦事項
    tasks[task_id] = task
    return jsonify({'message': f'task_id: {task_id} updated'}), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    # 檢查待辦事項是否存在
    if task_id < 0 or task_id >= len(tasks):
        return jsonify({'message': 'task not found'}), 404

    # 刪除待辦事項
    tasks.pop(task_id)
    return jsonify({'message': 'task deleted'}), 200

if __name__ == '__main__':
    # import ngrok
    # # listener = ngrok.forward(5000, authtoken_from_env=True)
    # listener = ngrok.connect(5000, authtoken='2GM3LTnHAagoYGegsvJ1EM541Or_4oqpJkuwFdjy7kqqvcRyk')#tw
    # print(f"Ingress established at {listener.url()}")
    app.run(debug=True)


# curl -X GET https://3aa7-2001-b400-e458-e4e0-94c1-410e-6780-cbf5.jp.ngrok.io/tasks
# curl -d '{"key2":"value1", "key2":"value2"}' -H "Content-Type: application/json" -X POST https://3aa7-2001-b400-e458-e4e0-94c1-410e-6780-cbf5.jp.ngrok.io/tasks