#coding: utf-8
from datetime import datetime
from .. import db

class TaskModel(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, default='')
    content = db.Column(db.Text)
    alerttime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    tag = db.Column(db.Text)
    status = db.Column(db.Integer)
    type = db.Column(db.Integer)
    group_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    created_by = db.Column(db.Integer, default=1)
    

    @staticmethod
    def insert_view(db, args):
        view = TaskModel(args)
        db.session.add(view)
        db.session.commit()

    @staticmethod
    def add_view(db):
        view = TaskModel.query.first()
        view.num_of_view += 1
        db.session.add(view)
        db.session.commit()

    @staticmethod
    def update_view(db, id, args):
        task = TaskModel.query.filter_by(id=id).first()
        if args.title != None:
            task.title = args.title
        if args.content != None:
            task.content = args.content
        if args.alerttime != None:
            task.alerttime = args.alerttime
        if args.tag != None:
            task.tag = args.tag
        if args.status != None:
            task.status = args.status
        if args.type != None:
            task.type = args.type
        if args.group_id != None:
            task.group_id = args.group_id
        db.session.add(task)
        db.session.commit()
        return TaskModel.query.filter_by(id=id).first()

    def __repr__(self):
        return '<TaskModel %r>' % self.title
    
    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict
