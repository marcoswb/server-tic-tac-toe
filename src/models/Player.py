from src.models.TableDynamoDB import TableDynamoDB


class Player(TableDynamoDB):

    def __init__(self):
        super().__init__('Player')

    def get_registered_users(self):
        data = self._get_all_itens()

        list_nicknames = []
        for item in data:
            list_nicknames.append(item.get('some_data').get('nickname'))

        return list_nicknames
