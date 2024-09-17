import boto3
from boto3.dynamodb.conditions import Key
import uuid


class TableDynamoDB:

    def __init__(self, table, name_primary_key):
        self.__table = table
        self.__name_primary_key = str(name_primary_key)
        self.__dyn_resource = boto3.resource('dynamodb')
        self.__data_register = {}

        self._create_table()

    def _get_dict_object(self):
        return self.__data_register

    def create_register(self, data, primary_key):
        self.__data_register = dict(data)
        self._save(primary_key)

    def _save(self, primary_key):
        table = self.__dyn_resource.Table(self.__table)

        table.put_item(
            Item={
                self.__name_primary_key: primary_key,
                'id': str(uuid.uuid4()),
                'some_data': self._get_dict_object(),
            }
        )

    def _create_table(self):
        if self.__table not in self._get_list_tables():
            params = self._get_params_table()
            table = self.__dyn_resource.create_table(**params)
            table.wait_until_exists()

    @staticmethod
    def _get_params_table():
        params = {}
        return params

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

    def _get_item_by_sort_key(self, key1, value1):
        table = self.__dyn_resource.Table(self.__table)

        response = table.query(
            KeyConditionExpression=Key(key1).eq(value1)
        )

        if len(response['Items']) > 0:
            return response['Items'][0]['some_data']
        else:
            return {}

    def _get_id_item(self, value_pk):
        table = self.__dyn_resource.Table(self.__table)

        response = table.query(
            KeyConditionExpression=Key(self.__name_primary_key).eq(value_pk)
        )

        if len(response['Items']) > 0:
            return response['Items'][0].get('id')
        else:
            return None

    def update_register(self, primary_key, key_update, new_value):
        try:
            table = self.__dyn_resource.Table(self.__table)
            id_value = self._get_id_item(primary_key)

            table.update_item(
                Key={self.__name_primary_key: primary_key, 'id': id_value},
                UpdateExpression=f"set some_data.{key_update} = :newValue",
                ExpressionAttributeValues={":newValue": new_value},
                ReturnValues="UPDATED_NEW"
            )

            return True
        except Exception as error:
            print(error)
            return False
