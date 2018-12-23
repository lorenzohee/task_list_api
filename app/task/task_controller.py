#coding:utf-8
import json
from flask import jsonify
from flask_restful import reqparse, abort, Api, Resource
from .task_model import TaskModel
from .. import db

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)

class TaskController(Resource):
    def get(self, id):
        task = TaskModel.query.get_or_404(id)
        return jsonify(task.to_json())

    def put(self, id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return { 'hello': 'put '+id}

    def delete(self, id):
        return { 'hello': 'delete' + id}

class TaskListController(Resource):
    def get(self):
        TaskModel.insert_view(db)
        list = TaskModel.query.order_by(TaskModel.id.desc())
        tmp = []
        for x in list:
            tmp.append(x.to_json())
        return jsonify(tmp)
    
    def post(self):
        TaskModel.insert_view(db)
        return {'hello': 'post'}