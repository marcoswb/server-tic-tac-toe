from flask_restful import Resource
from flask import request, Response

from src.models.Player import Player
from src.utils.ResponseJson import ResponseJson
from src.utils.functions import *


class Register(Resource):
    @staticmethod
    def post():
        message = dict(request.json)

        if not valid_json_input(message, ['name', 'nickname', 'password']):
            return ResponseJson(400, code_message=1).json()

        player = Player()
        player.set_name(message.get('name'))
        player.set_nickname(message.get('nickname'))
        player.set_password(message.get('password'))
        player.set_logged(False)
        player.set_playing(False)
        player.save()

        return ResponseJson(200).json()
