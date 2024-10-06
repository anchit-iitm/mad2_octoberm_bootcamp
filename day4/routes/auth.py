from flask import request, make_response, jsonify
from flask_restful import Resource

from models import user_datastore, db

# @app.route('/signup', methods=['POST'])
# def register():
class register(Resource):
    def post(self):
        data = request.json
        email = data.get('email')
        password = data.get('password')
        role = data.get('role') # if role is a string

        if not email:
            return make_response(jsonify({"status": "email is required"}), 400)
        if not password:
            return make_response(jsonify({"status": "password is required"}), 400)
        if not role:
            return make_response(jsonify({"status": "role is required"}), 400)
        
        if role == "admin":
            return make_response(jsonify({"status": "role cannot be admin"}), 400)
        
        if not user_datastore.find_user(email=email):
            # from flask_security import hash_password
            # hashed_password = hash_password(password)
            new_user = user_datastore.create_user(email=email, password=password, roles=[role])
            # user_datastore.add_role_to_user(new_user, role)
            if role == "manager":
                user_datastore.deactivate_user(new_user)    
            db.session.commit()
            return make_response(jsonify({"status": "success"}), 201)
        return make_response(jsonify({"status": "user already exists"}), 400)

# @app.route('/signin', methods=['POST'])
# def login():
class login(Resource):
    def post(self):
        data = request.json
        email = data.get('email')
        password = data.get('password')

        if not email:
            return make_response(jsonify({"status": "email is required"}), 400)
        if not password:
            return make_response(jsonify({"status": "password is required"}), 400)
        
        user = user_datastore.find_user(email=email)
        if user:
            if user.password == password: # from flask_security import verify_password / verify_password(password, user.password)
                token = user.get_auth_token()
                return make_response(jsonify({"status": "login successfully", "authToken": token}), 200)
            return make_response(jsonify({"status": "password is incorrect"}), 400)
        return make_response(jsonify({"status": "email doesnt exists"}), 400)
