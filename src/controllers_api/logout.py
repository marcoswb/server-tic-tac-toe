from flask_restful import Resource
from flask import request

from src.models.Player import Player
from src.utils.ResponseJson import ResponseJson
from src.utils.functions import *


class Logout(Resource):

    @staticmethod
    def post():
        message = dict(request.json)

        if not valid_json_input(message, ['nickname']):
            return ResponseJson(400, code_message=1).json()

        player = Player()
        nickname = str(message.get('nickname')).lower()

        registered_users = player.get_registered_users()
        if nickname not in registered_users:
            response = ResponseJson(400, code_message=3)
            response.add_key_in_return_message('users', registered_users)
            return response.json()

        logged = player.logout(message.get('nickname'))
        if logged:
            return ResponseJson(200).json()
        else:
            response = ResponseJson(400, code_message=5)
            return response.json()
