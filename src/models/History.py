from src.models.TableDynamoDB import TableDynamoDB


class History(TableDynamoDB):

    def __init__(self):
        self.__table_name = 'History'
        self.__name_primary_key = 'nickname'
        super().__init__('History', 'nickname')

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

    def get_history(self, nickname):
        data = self._get_all_itens()

        result = []
        for item in data:
            aux_item = item.get('some_data')
            if aux_item.get('nickname') == nickname:
                result.append(aux_item)

        return sorted(result, key=lambda d: d['time'])
