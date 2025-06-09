import json
import pytest

try:
    from flask import Flask, jsonify, request
except ModuleNotFoundError:
    Flask = None


@pytest.fixture
def app():
    if Flask is None:
        pytest.skip("Flask not installed")
    app = Flask(__name__)
    app.config['TESTING'] = True
    tasks = [
        {'id': 1, 'title': 'existing task'}
    ]

    @app.route('/tasks', methods=['GET'])
    def list_tasks():
        return jsonify(tasks)

    @app.route('/tasks', methods=['POST'])
    def add_task():
        task = request.json
        tasks.append(task)
        return jsonify(task), 201

    @app.route('/tasks/<int:task_id>', methods=['GET'])
    def get_task(task_id):
        for task in tasks:
            if task['id'] == task_id:
                return jsonify(task)
        return jsonify({'message': 'task not found'}), 404

    @app.route('/tasks/<int:task_id>', methods=['DELETE'])
    def delete_task(task_id):
        for i, task in enumerate(tasks):
            if task['id'] == task_id:
                tasks.pop(i)
                return jsonify({'message': 'task deleted'})
        return jsonify({'message': 'task not found'}), 404

    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_get_tasks(client):
    resp = client.get('/tasks')
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, list)
    assert len(data) == 1


def test_add_task(client):
    new_task = {'id': 2, 'title': 'new task'}
    resp = client.post('/tasks', json=new_task)
    assert resp.status_code == 201
    assert resp.get_json() == new_task

    resp = client.get('/tasks/2')
    assert resp.status_code == 200
    assert resp.get_json() == new_task

    resp = client.delete('/tasks/2')
    assert resp.status_code == 200
    assert resp.get_json()['message'] == 'task deleted'

    resp = client.get('/tasks/2')
    assert resp.status_code == 404
