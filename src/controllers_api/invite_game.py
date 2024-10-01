from flask_restful import Resource
from flask import request

from src.models.Queue import Queue
from src.utils.ResponseJson import ResponseJson
from src.utils.functions import *


class InviteGame(Resource):

    @staticmethod
    def get():
        nickname = request.args.get('nickname')
        if not nickname:
            return ResponseJson(400, code_message=7).json()

        queue = Queue()
        result = queue.get_invites(nickname)

        response = ResponseJson(200)
        response.add_key_in_return_message('invites', result)

        return response.json()

    @staticmethod
    def post():
        message = dict(request.json)

        if not valid_json_input(message, ['nickname', 'oponent']):
            return ResponseJson(400, code_message=1).json()

        queue = Queue()

        queue.create_register({
            'nickname': message.get('nickname'),
            'oponent': message.get('oponent'),
            'time': get_current_time()
        }, message.get('nickname'))

        return ResponseJson(200).json()
