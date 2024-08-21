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

        first_response = self.decode_message(socket_instance.recv(self.SIZE_BUFFER_PACKETS))
        print(first_response)
        while True:
            if first_response.get('message') == 'await':
                response = self.decode_message(socket_instance.recv(self.SIZE_BUFFER_PACKETS))
                print(f'MENSAGEM RETORNADA DO SERVIDOR {response}')

                action = response.get('action')
                if action != 'play':
                    print(response)
                    break

                message = input('Escreve alguma coisa: ')
                socket_instance.send(self.encode_message(message))

            elif first_response.get('message') == 'play':
                message = input('Escreve alguma coisa: ')
                socket_instance.send(self.encode_message(message))

                response = self.decode_message(socket_instance.recv(self.SIZE_BUFFER_PACKETS))
                print(f'MENSAGEM RETORNADA DO SERVIDOR {response}')

                action = response.get('action')
                if action != 'play':
                    print(response)
                    break

        socket_instance.close()

    def create_socket_instance(self):
        socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_instance.connect((self.host, self.port))

        return socket_instance

    def send_confirmation_message(self, socket_instance):
        message = 'entrar'
        socket_instance.send(self.encode_message(message, player='marcão monstro'))

    @staticmethod
    def decode_message(message):
        message.decode('utf8')
        return json.loads(message)

    @staticmethod
    def encode_message(message, action='play', player=''):
        data = {
            'message': message,
            'action': action,
            'player': player
        }

        return json.dumps(data).encode('utf-8')


if __name__ == '__main__':
    app = Client()
    app.start()
    print('ACABOUUUUU')
