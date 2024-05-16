import socket
from time import sleep
from threading import Thread

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
                response = socket_instance.recv(self.SIZE_BUFFER_PACKETS).decode('utf8')
                print(f'MENSAGEM RETORNADA DO SERVIDOR {response}')

                message = input('Escreve alguma coisa: ')
                socket_instance.send(message.encode('utf-8'))
            elif first_response == 'play':
                message = input('Escreve alguma coisa: ')
                socket_instance.send(message.encode('utf-8'))

                response = socket_instance.recv(self.SIZE_BUFFER_PACKETS).decode('utf8')
                print(f'MENSAGEM RETORNADA DO SERVIDOR {response}')
            else:
                break

    def create_socket_instance(self):
        socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_instance.connect((self.host, self.port))

        return socket_instance

    @staticmethod
    def send_confirmation_message(socket_instance):
        message = input('informe a palavra secreta: ')
        socket_instance.send(message.encode('utf-8'))


if __name__ == '__main__':
    app = Client()
    app.start()
    print('ACABOU')
