import socket
from time import sleep

host = '127.0.0.1'
port = 8000
messages = [
    'Iniciar',
    'Teste',
    'Teste 2',
    'Python 3'
]
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

for message in messages:
    client.send(str.encode(message))
    sleep(5)

print('passou')
