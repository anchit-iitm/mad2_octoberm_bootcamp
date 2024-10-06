from flask_sqlalchemy import SQLAlchemy # pip install flask_sqlalchemy

from flask_security import AsaList, UserMixin, RoleMixin, SQLAlchemyUserDatastore # pip install flask_security

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.mutable import MutableList


db = SQLAlchemy()

class mad1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    name1 = db.Column(db.String(100))

class mad2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('user.id'))
    role_id = db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))

class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255)) #

    permissions = Column(MutableList.as_mutable(AsaList()), nullable=True) #

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)  # required

    email = Column(String(255), unique=True)  # required
    username = Column(String(255), unique=True, nullable=True)
    password = Column(String(255), nullable=False)  # required

    last_login_at = Column(DateTime())
    current_login_at = Column(DateTime())
    last_login_ip = Column(String(100))
    current_login_ip = Column(String(100))
    login_count = Column(Integer)

    active = Column(Boolean())  # required
    fs_uniquifier = Column(String(64), unique=True, nullable=False)  # required

    confirmed_at = Column(DateTime())
    roles = relationship('Role', secondary='roles_users',
                         backref=backref('users', lazy='dynamic'))  # required
    
user_datastore = SQLAlchemyUserDatastore(db, User, Role)