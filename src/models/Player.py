from src.models.TableDynamoDB import TableDynamoDB
from src.utils.functions import password_match

class Player(TableDynamoDB):

    def __init__(self):
        self.__table_name = 'Player'
        self.__name_primary_key = 'nickname'
        super().__init__('Player', 'nickname')

    def _get_params_table(self):
        params = {
                'TableName': self.__table_name,
                'KeySchema': [
                    {'AttributeName': 'nickname', 'KeyType': 'HASH'},
                    {'AttributeName': 'id', 'KeyType': 'RANGE'}
                ],
                'AttributeDefinitions': [
                    {'AttributeName': 'nickname', 'AttributeType': 'S'},
                    {'AttributeName': 'id', 'AttributeType': 'S'}
                ],
                'ProvisionedThroughput': {'ReadCapacityUnits': 10, 'WriteCapacityUnits': 10},
            }

        return params

    def get_registered_users(self):
        data = self._get_all_itens()

        list_nicknames = []
        for item in data:
            list_nicknames.append(item.get('some_data').get('nickname'))

        return list_nicknames

    def get_free_users(self):
        data = self._get_all_itens()

        list_nicknames = []
        for item in data:
            aux_item = item.get('some_data')
            if aux_item.get('logged') and not aux_item.get('playing'):
                list_nicknames.append(aux_item.get('nickname'))

        return list_nicknames

    def check_password(self, nickname, password):
        data = self._get_item_by_sort_key('nickname', nickname)
        if password_match(data.get('password'), password):
            return True
        else:
            return False

    def login(self, nickname):
        response = self.update_register(nickname, 'logged', True)
        return response
