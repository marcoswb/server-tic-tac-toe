import boto3
import uuid
import random


class TableDynamoDB:

    def __init__(self, table):
        self.__table = table
        self.__dyn_resource = boto3.resource('dynamodb')
        self.__data_register = {}

        self._create_table()

    def _get_dict_object(self):
        return self.__data_register

    def create_register(self, data):
        self.__data_register = dict(data)
        self._save()

    def _save(self):
        table = self.__dyn_resource.Table(self.__table)

        table.put_item(
            Item={
                "id": str(uuid.uuid4()),
                "sort_key": random.randint(1, 100),
                "some_data": self._get_dict_object(),
            }
        )

    def _create_table(self):
        if self.__table not in self._get_list_tables():
            params = {
                'TableName': self.__table,
                'KeySchema': [
                    {'AttributeName': 'id', 'KeyType': 'HASH'},
                    {'AttributeName': 'sort_key', 'KeyType': 'RANGE'}
                ],
                'AttributeDefinitions': [
                    {'AttributeName': 'id', 'AttributeType': 'S'},
                    {'AttributeName': 'sort_key', 'AttributeType': 'N'}
                ],
                'ProvisionedThroughput': {'ReadCapacityUnits': 10, 'WriteCapacityUnits': 10},
            }
            table = self.__dyn_resource.create_table(**params)
            table.wait_until_exists()

    def _get_all_itens(self):
        table = self.__dyn_resource.Table(self.__table)

        response = table.scan()
        items = response['Items']

        # Continua o escaneamento se houver mais dados (paginação)
        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            items.extend(response['Items'])

        return items

    def _get_list_tables(self):
        """
        Return list of all tables database
        """
        tables = []
        for table in self.__dyn_resource.tables.all():
            tables.append(table.name)

        return tables
