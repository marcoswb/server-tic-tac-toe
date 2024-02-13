from threading import Thread

import src.utils.functions as func


class Client:

    def __init__(self, ip_client, client):
        """
        Class to handle client connection
        """
        self.__ip_client = ip_client
        self.__client = client
        self.SIZE_BUFFER_PACKETS = int(func.get_environment_variable('size_buffer_packets'))

        thread_client = Thread(target=self.handle_client)
        thread_client.start()

    def handle_client(self):
        print(f'Conectado a {self.__ip_client}')

        data = self.wait_for_data_client()
        if data == 'read':
            # SOCKET DE LEITURA
            print('socket de escrita')
        elif data == 'write':
            # SOCKET DE ESCRITA
            print('socket de leitura')

        while data:
            data = self.wait_for_data_client()
            print(data)

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
