from flask_restful import Resource
from flask import request, Response


class Register(Resource):
    @staticmethod
    def post():
        message = request.json
        print(message)

        return Response(status=200, mimetype='application/json')