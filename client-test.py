import socket
import json

import src.utils.functions as func


class Client:

    def __init__(self):
        self.host = func.get_environment_variable('host')
        self.port = int(func.get_environment_variable('port'))
        self.SIZE_BUFFER_PACKETS = int(func.get_environment_variable('size_buffer_packets'))

    def start(self):
        print('abrir o socket')
        socket_instance = self.create_socket_instance()

        self.send_confirmation_message(socket_instance)

        first_response = socket_instance.recv(self.SIZE_BUFFER_PACKETS).decode('utf8')
        while True:
            if first_response == 'await':
                response = self.decode_message(socket_instance.recv(self.SIZE_BUFFER_PACKETS))
                print(f'MENSAGEM RETORNADA DO SERVIDOR {response}')

                if response.get('action') == 'end_game':
                    break

                message = input('Escreve alguma coisa: ')
                socket_instance.send(self.encode_message(message))
            elif first_response == 'play':
                message = input('Escreve alguma coisa: ')
                socket_instance.send(self.encode_message(message))

                response = self.decode_message(socket_instance.recv(self.SIZE_BUFFER_PACKETS))
                print(f'MENSAGEM RETORNADA DO SERVIDOR {response}')

                if response.get('action') == 'end_game':
                    break

        socket_instance.close()

    def create_socket_instance(self):
        socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_instance.connect((self.host, self.port))

        return socket_instance

    @staticmethod
    def send_confirmation_message(socket_instance):
        message = input('informe a palavra secreta: ')
        socket_instance.send(message.encode('utf-8'))

    @staticmethod
    def decode_message(message):
        message.decode('utf8')
        return json.loads(message)

    @staticmethod
    def encode_message(message, action='play'):
        data = {
            'message': message,
            'action': action
        }

        return json.dumps(data).encode('utf-8')


if __name__ == '__main__':
    app = Client()
    app.start()
    print('ACABOUUUUU')
