from src.models.TableDynamoDB import TableDynamoDB


class Queue(TableDynamoDB):

    def __init__(self):
        self.__table_name = 'Queue'
        self.__name_primary_key = 'nickname'
        super().__init__('Queue', 'nickname')

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

    def get_invites(self, nickname):
        data = self._get_all_itens()

        list_nicknames = []
        for item in data:
            if item.get('some_data').get('nickname') != nickname:
                list_nicknames.append(item.get('some_data').get('oponent'))

        return list_nicknames
