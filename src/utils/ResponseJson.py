from flask import Response
import json

from src.utils.messages import messages


class ResponseJson:

    def __init__(self, status_code, code_message=''):
        self.__status_code = int(status_code)
        self.__response_headers = {'Content-Type': 'application/json'}
        self.__data = {}

        if code_message:
            self.__data = messages.get(int(code_message))

    def add_key_in_return_message(self, key, value):
        self.__data[key] = value

    def json(self):
        if self.__data:
            return Response(response=json.dumps(self.__data), status=self.__status_code, headers=self.__response_headers)
        else:
            return Response(status=self.__status_code, headers=self.__response_headers)
