from flask_restful import reqparse, abort, Api, Resource

TODOS = [{"id": 1, "title": 'name', "content": 'good', "status": 1, "type": 2},{"id": 2, "title": 'name2', "content": 'good', "status": 1, "type": 2}]

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

class TaskListController(Resource):
	def get(self):
		return TODOS

	def post(self):
		return {}

class TaskController(Resource):
	def get(self, task_id):
		abort_if_todo_doesnt_exist(task_id)
		return TODOS[task_id]

	def put(self, task_id):
		args = parser.parse_args()
		task = {'task': args['task']}
		TODOS[task_id] = task
		return task, 201

	def delete(self, task_id):
		abort_if_todo_doesnt_exist(task_id)
		del TODOS[task_id]
		return '', 204