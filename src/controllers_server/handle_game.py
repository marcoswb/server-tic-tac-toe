from random import randint

from src.controllers_server.handle_client import Client


class Game:

    def __init__(self):
        self.__player_01 = Client()
        self.__player_02 = Client()

    def set_players(self, player_01, player_02):
        """
        Set players to game
        """
        # player_01 sempre inicia o jogo, então preenche de forma aleatória o jogador 01
        random_number = randint(1, 2)

        if random_number == 1:
            self.__player_01.init(player_01[1], player_01[0])
            self.__player_02.init(player_02[1], player_02[0])
        else:
            self.__player_01.init(player_02[1], player_02[0])
            self.__player_02.init(player_01[1], player_01[0])

    def start_game(self):
        print('iniciar jogo', self.__player_01.get_ip_client(), self.__player_02.get_ip_client())

        # informar os jogadores quem vai começar
        self.__player_01.send_data('play')
        self.__player_02.send_data('await')

        while True:
            instruction = self.__player_01.wait_for_data_client()
            self.__player_02.send_data(instruction)

            instruction = self.__player_02.wait_for_data_client()
            self.__player_01.send_data(instruction)
