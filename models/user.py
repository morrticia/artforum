from db import db
import uuid


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def idgenerator(cls):
        cls._id = uuid.uuid4().node
        return cls._id

    @classmethod
    def find_by_username(cls, username):
        return UserModel.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, id):
        return UserModel.query.filter_by(id=id).first()

    def add_account(self):
        db.session.add(self)
        db.session.commit()

    def delete_account(self):
        db.session.delete(self)
        db.session.commit()

