from flask_restful import Resource
from flask import request

from src.models.Player import Player
from src.utils.ResponseJson import ResponseJson
from src.utils.functions import *


class UserFree(Resource):

    @staticmethod
    def get():
        player = Player()

        free_users = player.get_free_users()
        if free_users:
            response = ResponseJson(200)
            response.add_key_in_return_message('users', free_users)
            return response.json()
        else:
            response = ResponseJson(400, code_message=6)
            return response.json()
