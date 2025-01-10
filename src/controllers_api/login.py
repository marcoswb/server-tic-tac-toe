from flask_restful import Resource
from flask import request

from src.models.Player import Player
from src.utils.ResponseJson import ResponseJson
from src.utils.functions import *


class Login(Resource):

    @staticmethod
    def post():
        message = dict(request.json)

        if not valid_json_input(message, ['nickname', 'password']):
            return ResponseJson(400, code_message=1).json()

        player = Player()
        nickname = str(message.get('nickname')).lower()

        registered_users = player.get_registered_users()
        if nickname not in registered_users:
            response = ResponseJson(400, code_message=3)
            response.add_key_in_return_message('users', registered_users)
            return response.json()

        correct_password = player.check_password(message.get('nickname'), message.get('password'))
        if not correct_password:
            response = ResponseJson(400, code_message=4)
            return response.json()

        socket_key = player.login(message.get('nickname'))
        if socket_key:
            response = ResponseJson(200)
            response.add_key_in_return_message('socket_key', socket_key)
            return response.json()
        else:
            response = ResponseJson(400, code_message=5)
            return response.json()
