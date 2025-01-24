import socket
from pathlib import Path
from utils import extract_route, read_file

CUR_DIR = Path(__file__).parent
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080

RESPONSE_TEMPLATE = '''HTTP/1.1 200 OK

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Get-it</title>
</head>
<body>

<img src="img/logo-getit.png">
<p>Como o Post-it, mas com outro verbo</p>

<ul>
  <li>
    <h3>Receita de miojo</h3>
    <p>Bata com um martelo antes de abrir o pacote. Misture o tempero, coloque em uma vasilha e aproveite seu snack :)</p>
  </li>
  <li>
    <h3>Pão doce</h3>
    <p>Abra o pão e coloque o seu suco em pó favorito.</p>
  </li>
  <li>
    <h3>Sorvete com cristais de leite</h3>
    <p>Sirva o seu sorvete favorito em uma vasilha e jogue leite em cima.</p>
  </li>
  <li>
    <h3>Iogurte natural</h3>
    <p>Deixe o leite fora da geladeira (esse é mentira, não faça isso).</p>
  </li>
  <li>
    <h3>Homer Simpson</h3>
    <p>~( 8(|)</p>
  </li>
  <li>
    <h3>Numero mágico</h3>
    <p>142857</p>
  </li>
  <li>
    <h3>Série da Fundação - Isaac Asimov</h3>
    <p>É boa, leia.</p>
  </li>
</ul>

</body>
</html>
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
