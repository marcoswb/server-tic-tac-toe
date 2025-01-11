from flask_restful import Resource

from src.models.Player import Player
from src.utils.ResponseJson import ResponseJson


class UserStatus(Resource):

    @staticmethod
    def get():
        player = Player()
        result = player.get_user_status()
        if result:
            response = ResponseJson(200)
            response.add_key_in_return_message('status', result)

            return response.json()
        else:
            response = ResponseJson(400, code_message=6)
            return response.json()
