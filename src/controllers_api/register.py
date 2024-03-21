from flask_restful import Resource
from flask import request, Response

from src.models.Player import Player


class Register(Resource):
    @staticmethod
    def post():
        message = request.json

        player = Player()
        player.set_nickname('marcos')
        player.set_password('teste')
        player.set_logged(False)
        player.set_playing(False)
        player.save()

        return Response(status=200, mimetype='application/json')
