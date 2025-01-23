import socket
from pathlib import Path
from utils import extract_route, read_file

CUR_DIR = Path(__file__).parent
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080

RESPONSE_TEMPLATE = '''
HTML apagado por questão de espaço, mas você deve manter o código anterior aqui.
'''

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()

print(f'Servidor escutando em (ctrl+click): http://{SERVER_HOST}:{SERVER_PORT}')

while True:
    client_connection, client_address = server_socket.accept()

    request = client_connection.recv(1024).decode()
    print('*'*100)
    print(request)

    route = extract_route(request)
    filepath = CUR_DIR / route
    if filepath.is_file():
        response = 'HTTP/1.1 200 OK\n\n'.encode() + read_file(filepath)
    else:
        response = RESPONSE_TEMPLATE.encode()
    client_connection.sendall(response)

    client_connection.close()

server_socket.close()
