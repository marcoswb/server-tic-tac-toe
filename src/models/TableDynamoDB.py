import boto3
import uuid
import random


class TableDynamoDB:

    def __init__(self, table):
        self.__table = table
        self.__dyn_resource = boto3.resource('dynamodb')

        self.create_table()

    @staticmethod
    def get_dict_object():
        return {}

    def save(self):
        table = self.__dyn_resource.Table(self.__table)

        table.put_item(
            Item={
                "id": str(uuid.uuid4()),
                "sort_key": random.randint(1, 100),
                "some_data": self.get_dict_object(),
            }
        )

    def create_table(self):
        if self.__table not in self.get_list_tables():
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

    def get_list_tables(self):
        """
        Return list of all tables database
        """
        tables = []
        for table in self.__dyn_resource.tables.all():
            tables.append(table)

        return tables
