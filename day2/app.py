from flask import Flask, render_template, request  # pip install flask

from flask_sqlalchemy import SQLAlchemy # pip install flask_sqlalchemy

from flask_security import Security, AsaList, UserMixin, RoleMixin, SQLAlchemyUserDatastore # pip install flask_security

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.mutable import MutableList

app = Flask(__name__)

app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite3'

app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_PASSWORD_SALT'] = 'salt'

db = SQLAlchemy(app)


class mad1(db.Model):
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
    description = Column(String(255))
    permissions = Column(MutableList.as_mutable(AsaList()), nullable=True)

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    username = Column(String(255), unique=True, nullable=True)
    password = Column(String(255), nullable=False)
    last_login_at = Column(DateTime())
    current_login_at = Column(DateTime())
    last_login_ip = Column(String(100))
    current_login_ip = Column(String(100))
    login_count = Column(Integer)
    active = Column(Boolean())
    fs_uniquifier = Column(String(64), unique=True, nullable=False)
    confirmed_at = Column(DateTime())
    roles = relationship('Role', secondary='roles_users',
                         backref=backref('users', lazy='dynamic'))
    

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


with app.app_context():
    db.create_all()

@app.route('/test', methods=['GET', 'POST'])
def test1():
    if request.method == 'POST':
        data = request.form.get('name')
        print(data)
        new_data = mad1(name=data)
        db.session.add(new_data)
        db.session.commit()
        return "success"
    var1 = 'this is coming from the backend'
    return render_template('test.html', var2=var1)

@app.route('/version2')
def testjson():
    var1 = 'this is coming from the backend'
    return {"var2": var1}

@app.route('/version3', methods=['POST'])
def postjson():
    # data = request.form.get('name')
    print(request.json)
    data = request.json.get('key_name')
    print(data)
    if not data:
        return {"status": "failure"}
    new_data = mad1(name=data)
    db.session.add(new_data)
    db.session.commit()
    return {"status": "success"}


# get is to send data from backend to frontend  /  whenever we hit a url in the browser, it is a get request
# post is to send data from frontend to backend
# put is to update data in the backend from frontend  / patch is similar to put
# delete is to delete data in the backend


if __name__ == '__main__':
    app.run()