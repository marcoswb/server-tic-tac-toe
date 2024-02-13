from time import sleep


class Server:

    def __init__(self):
        self.__default_port = 8000

    def start(self):
        print(f'Servidor executando na porta {self.__default_port}, para parar precione CTRL + C.')


if __name__ == '__main__':
    app = Server()
    app.start()

    while True:
        sleep(1)
