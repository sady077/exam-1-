from flask_login import UserMixin

from . import db


# @login_manager.user_loader
# def load_user(id):
#     return User.query.get(int(id))

class Position(db.Model):
    name = db.Column(db.String)
    department = db.Column(db.String)
    wage = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f'{self.name} - {self.wage}'

class Employee(db.Model):
    name = db.Column(db.String)
    inn = db.Column(db.String)
    position = db.relationship(db.String, db.ForeignKey('Category',backref=db.backref('emoloyee', lazy='dynamic')))
    position_id = db.Column(db.Integer, db.ForeignKey('category.id'))


class User(UserMixin, db.Model):
    username = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String)

    @property
    def password(self):
        return self.password_hash





#
# class Position(db.Model):
#     pass
#
#
# class Employee(db.Model):
#     pass
#
#
# class User(UserMixin, db.Model):
#     pass
