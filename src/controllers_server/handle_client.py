import src.utils.functions as func


class Client:

    def __init__(self):
        """
        Class to handle client connection
        """
        self.__ip_client = None
        self.__client = None
        self.SIZE_BUFFER_PACKETS = int(func.get_environment_variable('size_buffer_packets'))

    def init(self, ip_client, client):
        self.__ip_client = ip_client
        self.__client = client

    def wait_for_data_client(self):
        """
        Return the data that the client sent
        """
        response = self.__client.recv(self.SIZE_BUFFER_PACKETS).decode('utf8')
        return response

    def send_data(self, instruction):
        self.__client.sendall(str(instruction).encode('utf-8'))

    def get_ip_client(self):
        return self.__ip_client

    def get_connection(self):
        return self.__client

    def close_client(self):
        print(f'Conexão com o client {self.__ip_client} finalizada')
        self.__client.close()
