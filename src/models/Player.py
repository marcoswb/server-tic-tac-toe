from src.models.TableDynamoDB import TableDynamoDB


class Player(TableDynamoDB):

    def __init__(self):
        super().__init__('Player')
        self.__id = None
        self.__name = None
        self.__nickname = None
        self.__password = None
        self.__logged = None
        self.__playing = None

    def get_dict_object(self):
        return {
            'id': self.__id,
            'name': self.__name,
            'nickname': self.__nickname,
            'password': self.__password,
            'logged': self.__logged,
            'playing': self.__playing
        }

    def set_name(self, name):
        self.__name = name

    def set_nickname(self, nickname):
        self.__nickname = nickname

    def set_password(self, password):
        self.__password = password

    def set_logged(self, logged ):
        self.__logged = logged

    def set_playing(self, playing):
        self.__playing = playing
