from flask_restful import Resource
from flask import request

from src.models.History import History as HistoryModel
from src.utils.ResponseJson import ResponseJson
from src.utils.functions import *


class History(Resource):

    @staticmethod
    def get():
        history = HistoryModel()
        nickname = request.args.get('nickname')
        if not nickname:
            return ResponseJson(400, code_message=7).json()

        result = history.get_history(nickname)

        response = ResponseJson(200)
        response.add_key_in_return_message('history', result)

        return response.json()

    @staticmethod
    def post():
        message = dict(request.json)

        if not valid_json_input(message, ['nickname', 'oponent', 'result']):
            return ResponseJson(400, code_message=1).json()

        history = HistoryModel()
        history.create_register({
            'nickname': message.get('nickname'),
            'oponent': message.get('oponent'),
            'result': message.get('result'),
            'time': get_current_time()
        }, message.get('nickname'))

        return ResponseJson(200).json()
