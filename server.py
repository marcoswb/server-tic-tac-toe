import datetime
import json
import socket
import selectors
from threading import Thread

from src.controllers_server.handle_game import Game
import src.utils.functions as func
from src.models.Player import Player


class Server:

    def __init__(self):
        self.HOST = func.get_environment_variable('host')
        self.DEFAULT_PORT = int(func.get_environment_variable('port'))
        self.SIZE_BUFFER_PACKETS = int(func.get_environment_variable('size_buffer_packets'))
        self.__player_01 = None
        self.__player_02 = None
        self.__challenged_users = {}

    def start(self):
        """
        Starts the server and waits for clients to connect
        """
        # start server
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.HOST, self.DEFAULT_PORT))
        server.listen()
        print(f'listening on {self.HOST}:{self.DEFAULT_PORT}')

        # register server in selector
        selector = selectors.DefaultSelector()
        selector.register(server, selectors.EVENT_READ, self.accept_connection)

        try:
            # wait a new connections
            while True:
                events = selector.select()
                for key, _ in events:
                    sock = key.fileobj
                    callback = key.data
                    callback(sock)

        except KeyboardInterrupt:
            print('Caught keyboard interrupt, exiting')
        finally:
            selector.close()

    def accept_connection(self, server):
        """
        Accepts connections from clients
        """
        client, address = server.accept()
        ip_client = address[0]

        confirm, nickname, opponent = self.confirm_identity(client)
        if not confirm:
            client.close()
            return

        if opponent == 'random':
            if not self.__player_01:
                self.__player_01 = (client, ip_client, nickname)
            else:
                self.__player_02 = (client, ip_client, nickname)

                Thread(target=self.start_game, args=(self.__player_01, self.__player_02, )).start()
                self.__player_01 = None
                self.__player_02 = None
        else:
            if self.__challenged_users.get(nickname):
                player_01 = self.__challenged_users.get(nickname)
                player_02 = (client, ip_client, nickname)
                Thread(target=self.start_game, args=(player_01, player_02, )).start()
                self.__challenged_users.pop(nickname)
            else:
                self.__challenged_users[opponent] = (client, ip_client, nickname)


    def confirm_identity(self, client):
        """
        Wait for the confirmation message from client
        """
        response = json.loads(client.recv(self.SIZE_BUFFER_PACKETS).decode('utf8'))
        nickname = response.get('player')
        opponent = response.get('opponent')

        authentication_client = response.get('socket_key')
        original_socket_key = Player().get_socket_key(nickname)

        if authentication_client == original_socket_key:
            return True, nickname, opponent
        else:
            return False, nickname, opponent

    @staticmethod
    def start_game(player_01, player_02):
        game = Game()
        game.set_players(player_01, player_02)
        game.start_game()


if __name__ == '__main__':
    app = Server()
    app.start()
