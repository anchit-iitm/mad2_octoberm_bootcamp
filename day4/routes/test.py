from flask import make_response, jsonify
from flask_restful import Resource

class test(Resource):
    def get(self):
        return make_response(jsonify({"status": "get req"}), 200)
    def post(self):
        return make_response(jsonify({"status": "post req"}), 200)
    def put(self):
        return make_response(jsonify({"status": "put req"}), 200)
    def delete(self):
        return make_response(jsonify({"status": "delete req"}), 200)
    
# @app.route('/version2')
# @auth_required('token')
# # @auth_token_required

# @roles_accepted('admin', 'manager', 'customer')
# # @roles_required('admin') / @roles_required('admin', 'manager')

class version2(Resource):
    from flask_security import auth_required, roles_accepted
    @auth_required('token')
    @roles_accepted('admin', 'manager')
    def get(self):
        var1 = 'this is coming from the backend, restful'
        from flask_security import current_user
        return make_response(jsonify({"var2": var1, "email": current_user.email}), 200)