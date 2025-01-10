from flask_restful import Resource
from flask import request

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
        nickname = str(message.get('nickname')).lower()

        registered_users = player.get_registered_users()
        if nickname in registered_users:
            response = ResponseJson(400, code_message=2)
            response.add_key_in_return_message('users', registered_users)
            return response.json()

        player.create_register({
            'name': message.get('name'),
            'nickname': message.get('nickname'),
            'password': encrypt_password(message.get('password')),
            'logged': False,
            'playing': False,
            'socket_key': ''
        }, message.get('nickname'))

        return ResponseJson(200).json()
