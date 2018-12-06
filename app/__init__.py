from flask import Flask
from flask_restful import Resource, Api
# from config import Config

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

def create_app():
    app = Flask(__name__)
    # app.config.from_object(Config)
    # Config.init_app(app)


    api = Api(app)
    api.add_resource(HelloWorld, '/')

    return app
