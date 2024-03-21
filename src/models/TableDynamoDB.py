import boto3


class TableDynamoDB:

    def __init__(self, table):
        self.__table = table

    @staticmethod
    def get_dict_object():
        return {}

    def save(self):
        dyn_resource = boto3.resource('dynamodb')
        table = dyn_resource.Table(self.__table)

        table.put_item(
            Item={
                "partition_key": 3,
                "sort_key": 3,
                "some_data": self.get_dict_object(),
            }
        )
