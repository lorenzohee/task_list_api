#coding: utf-8
from datetime import datetime
from .. import db

class TaskModel(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, default='0')

    @staticmethod
    def insert_view(db):
        view = TaskModel(title='good')
        db.session.add(view)
        db.session.commit()

    @staticmethod
    def add_view(db):
        view = TaskModel.query.first()
        view.num_of_view += 1
        db.session.add(view)
        db.session.commit()

    @staticmethod
    def update_view(db, id, task):
        view = TaskModel.query.get_or_404(id)
        view.title = task.title
        db.session.add(view)
        db.session.commit()

    def __repr__(self):
        return '<TaskModel %r>' % self.title
    
    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict
