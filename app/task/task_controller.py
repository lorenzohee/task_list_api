#coding:utf-8
import json
from flask import jsonify
from flask_restful import fields, marshal_with, reqparse, abort, Api, Resource
from .task_model import TaskModel
from .. import db

task_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'content': fields.String,
    'tag': fields.String,
    'task_type': fields.Integer,
    'status': fields.Integer,
    'alerttime': fields.Integer,
    'created_at': fields.DateTime
}

class TaskController(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument( 'title', dest='title', type=str, location='json')
        self.parser.add_argument( 'content', dest='content', type=str, location='json')
        self.parser.add_argument( 'alerttime', dest='alerttime', type=str, location='json' )
        self.parser.add_argument( 'tag', dest='tag', type=str, location='json' )
        self.parser.add_argument( 'status', dest='status', type=int, location='json' )
        self.parser.add_argument( 'group_id', dest='group_id', type=int, location='json' )
        self.parser.add_argument( 'task_type', dest='type', type=int, location='json' )
        super(TaskController, self).__init__()

    @marshal_with(task_fields)
    def get(self, id):
        task = TaskModel.query.get_or_404(id)
        return task

    @marshal_with(task_fields)
    def put(self, id):
        args = self.parser.parse_args()
        task = TaskModel.update_view(db, id, args)
        return task

    @marshal_with(task_fields)
    def delete(self, id):
        return TaskModel.delete_view(db, id)

class TaskListController(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument( 'title', dest='title', type=str, location='json', help = 'No task title provided', required=True)
        self.parser.add_argument( 'content', dest='content', type=str, location='json')
        self.parser.add_argument( 'alerttime', dest='alerttime', type=str, location='json' )
        self.parser.add_argument( 'tag', dest='tag', type=str, location='json' )
        self.parser.add_argument( 'task_type', dest='type', type=int, location='json' )
        super(TaskListController, self).__init__()

    def get(self):
        list = TaskModel.query.order_by(TaskModel.id.desc())
        tmp = []
        for x in list:
            tmp.append(x.to_json())
        return jsonify(tmp)
    
    @marshal_with(task_fields)
    def post(self):
        args = self.parser.parse_args()
        task = TaskModel.insert_view(db, args)
        return task