import socket
from time import sleep
from threading import Thread

import src.utils.functions as func


class Client:

    def __init__(self):
        self.host = func.get_environment_variable('host')
        self.port = int(func.get_environment_variable('port'))
        self.SIZE_BUFFER_PACKETS = int(func.get_environment_variable('size_buffer_packets'))
        self.messages = [
            'Iniciar',
            'Teste',
            'Teste 2',
            'Python 3'
        ]

        self.socket_instance_read = None
        self.socket_instance_write = None

    def start(self):
        self.socket_instance_read = self.create_socket_instance()
        print('abriu o socket')

        first_response = self.socket_instance_read.recv(self.SIZE_BUFFER_PACKETS).decode('utf8')
        while True:
            if first_response == 'await':
                response = self.socket_instance_read.recv(self.SIZE_BUFFER_PACKETS).decode('utf8')
                print(f'MENSAGEM RETORNADA DO SERVIDOR {response}')

                message = input('Escreve alguma coisa: ')
                self.socket_instance_read.send(message.encode('utf-8'))
            else:
                message = input('Escreve alguma coisa: ')
                self.socket_instance_read.send(message.encode('utf-8'))

                response = self.socket_instance_read.recv(self.SIZE_BUFFER_PACKETS).decode('utf8')
                print(f'MENSAGEM RETORNADA DO SERVIDOR {response}')

        # sleep(10)
        # self.socket_instance_write = self.create_socket_instance('write')
        # print('abriu o socket de escrita')
        #
        # thread_read_message = Thread(target=self.read_messages)
        # thread_read_message.start()
        #
        # thread_write_message = Thread(target=self.send_messages)
        # thread_write_message.start()

        while True:
            pass

    def create_socket_instance(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.host, self.port))
        # client.send(str.encode(message))

        return client

    def send_messages(self):
        for message in self.messages:
            self.socket_instance_write.send(str.encode(message))
            sleep(5)

    def read_messages(self):
        while True:
            response = self.socket_instance_read.recv(self.SIZE_BUFFER_PACKETS).decode('utf8')
            print(f'MENSAGEM RETORNADA DO SERVIDOR {response}')


if __name__ == '__main__':
    app = Client()
    app.start()
    print('ACABOU')
