from flask_restful import Resource
from flask import request, Response

from src.models.Player import Player


class Register(Resource):
    @staticmethod
    def post():
        message = dict(request.json)

        player = Player()
        player.set_name(message.get('name'))
        player.set_nickname(message.get('nickname'))
        player.set_password(message.get('password'))
        player.set_logged(False)
        player.set_playing(False)
        player.save()

        return Response(status=200, mimetype='application/json')
