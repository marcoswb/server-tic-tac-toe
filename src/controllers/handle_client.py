import json


class Client:

    def __init__(self, ip_client, client):
        """
        Class to handle client connection
        """
        self.SIZE_BUFFER_PACKETS = 1024
        self.__ip_client = ip_client
        self.__client = client

        self.handle_client()

    def handle_client(self):
        print(f'Conectado a {self.__ip_client}')

        data = self.wait_for_data_client()
        while data:
            print(data)
            data = self.wait_for_data_client()

        self.close_client()

    def wait_for_data_client(self):
        """
        Return the data that the client sent
        """
        response = self.__client.recv(self.SIZE_BUFFER_PACKETS).decode('utf8')
        return response

    def close_client(self):
        print(f'Conexão com o client {self.__ip_client} finalizada')
        self.__client.close()
