class Client:

    def __init__(self, ip_client, client):
        """
        Class to handle client connection
        """
        self.__ip_client = ip_client
        self.__client = client

        self.handle_client()

    def handle_client(self):
        print(f'Conectado a {self.__ip_client}')
