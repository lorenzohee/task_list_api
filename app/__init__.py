from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

from .task import TaskController, TaskListController
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Config.init_app(app)

    db.init_app(app)
    api = Api(app)
    api.add_resource(HelloWorld, '/hello', endpoint = 'helo')
    api.add_resource(TaskListController, '/tasks', endpoint = 'tasklist')
    api.add_resource(TaskController, '/tasks/<string:id>', endpoint = 'task')

    return app
