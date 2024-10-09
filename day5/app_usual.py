from flask import render_template, request  # pip install flask

from flask_security import auth_required, auth_token_required, roles_accepted, roles_required, current_user

from models import db, user_datastore, mad1

def create_app():
    from flask import Flask
    init_app = Flask(__name__)

    from config import LocalDev
    init_app.config.from_object(LocalDev)

    # db = SQLAlchemy(app)
    db.init_app(init_app)

    from flask_security import Security # pip install flask_security
    security = Security(init_app, user_datastore)

    return init_app

app = create_app()

@app.route('/test', methods=['GET', 'POST'])
def test1():
    if request.method == 'POST':
        data = request.form.get('name')
        print(data)
        from models import mad1
        new_data = mad1(name=data)
        db.session.add(new_data)
        db.session.commit()
        return "success"
    var1 = 'this is coming from the backend'
    return render_template('test.html', var2=var1)

@app.route('/version2')
@auth_required('token')
# @auth_token_required

@roles_accepted('admin', 'manager', 'customer')
# @roles_required('admin') / @roles_required('admin', 'manager')
def testjson():
    var1 = 'this is coming from the backend'
    return {"var2": var1, "email": current_user.email}

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

@app.route('/signup', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    role = data.get('role') # if role is a string

    if not email:
        return {"status": "email is required"}, 400
    if not password:
        return {"status": "password is required"}, 400
    if not role:
        return {"status": "role is required"}, 400
    
    if role == "admin":
        return {"status": "role cannot be admin"}, 400
    
    if not user_datastore.find_user(email=email):
        # from flask_security import hash_password
        # hashed_password = hash_password(password)
        new_user = user_datastore.create_user(email=email, password=password, roles=[role])
        # user_datastore.add_role_to_user(new_user, role)
        if role == "manager":
            user_datastore.deactivate_user(new_user)    
        db.session.commit()
        return {"status": "success"}, 201
    return {"status": "user already exists"}, 400

@app.route('/signin', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email:
        return {"status": "email is required"}, 400
    if not password:
        return {"status": "password is required"}, 400
    
    user = user_datastore.find_user(email=email)
    if user:
        if user.password == password: # from flask_security import verify_password / verify_password(password, user.password)
            token = user.get_auth_token()
            return {"status": "login successfully", "authToken": token}, 200
        return {"status": "password is incorrect"}, 400
    return {"status": "email doesnt exists"}, 400

# get is to send data from backend to frontend  /  whenever we hit a url in the browser, it is a get request
# post is to send data from frontend to backend
# put is to update data in the backend from frontend  / patch is similar to put
# delete is to delete data in the backend


if __name__ == '__main__':
    app.run()