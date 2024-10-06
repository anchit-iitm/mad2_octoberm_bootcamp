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