import socket
import selectors

from src.controllers.handle_client import Client
import src.utils.functions as func


class Server:

    def __init__(self):
        self.HOST = func.get_environment_variable('host')
        self.DEFAULT_PORT = int(func.get_environment_variable('port'))

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

    @staticmethod
    def accept_connection(server):
        """
        Accepts connections from clients
        """
        client, address = server.accept()
        ip_client = address[0]
        Client(ip_client, client)


if __name__ == '__main__':
    app = Server()
    app.start()
