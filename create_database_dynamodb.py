import boto3

dyn_resource = boto3.resource('dynamodb')


def create_user_table():
    table_name = 'Player'
    params = {
        'TableName': table_name,
        'KeySchema': [
            {'AttributeName': 'partition_key', 'KeyType': 'HASH'},
            {'AttributeName': 'sort_key', 'KeyType': 'RANGE'}
        ],
        'AttributeDefinitions': [
            {'AttributeName': 'partition_key', 'AttributeType': 'N'},
            {'AttributeName': 'sort_key', 'AttributeType': 'N'}
        ],
        'ProvisionedThroughput': {'ReadCapacityUnits': 10, 'WriteCapacityUnits': 10},
    }
    table = dyn_resource.create_table(**params)
    print(f'Criando {table_name}...')
    table.wait_until_exists()
    return table


if __name__ == '__main__':
    create_user_table()
    print('Tabelas criadas')
