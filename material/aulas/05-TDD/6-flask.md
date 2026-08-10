# Testando APIs Flask com pytest e Mocks

Assim como qualquer outro código, APIs Flask precisam ser testadas para garantir que funcionem corretamente. No entanto, testar APIs que dependem de um banco de dados real pode ser complicado. Felizmente, já temos todas as ferramentas necessárias!

Para esse exemplo, vamos considerar a seguinte API Flask:

```python
from flask import Flask, request
import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .cred (se disponível)
load_dotenv('.cred')

# Configurações para conexão com o banco de dados usando variáveis de ambiente
config = {
    'host': os.getenv('DB_HOST', 'localhost'),  # Obtém o host do banco de dados da variável de ambiente
    'user': os.getenv('DB_USER'),  # Obtém o usuário do banco de dados da variável de ambiente
    'password': os.getenv('DB_PASSWORD'),  # Obtém a senha do banco de dados da variável de ambiente
    'database': os.getenv('DB_NAME', 'db_escola'),  # Obtém o nome do banco de dados da variável de ambiente
    'port': int(os.getenv('DB_PORT', 3306)),  # Obtém a porta do banco de dados da variável de ambiente
    'ssl_ca': os.getenv('SSL_CA_PATH')  # Caminho para o certificado SSL
}


# Função para conectar ao banco de dados
def connect_db():
    """Estabelece a conexão com o banco de dados usando as configurações fornecidas."""
    try:
        # Tenta estabelecer a conexão com o banco de dados usando mysql-connector-python
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            return conn
    except Error as err:
        # Em caso de erro, imprime a mensagem de erro
        print(f"Erro: {err}")
        return None


app = Flask(__name__)


@app.route('/alunos', methods=['GET'])
def get_alunos():

    # conectar com a base de dados
    conn = connect_db()

    if conn is None:
        resp = {"erro": "Erro ao conectar ao banco de dados"}
        return resp, 500
    
    # se chegou até aqui, tenho uma conexão válida
    cursor = conn.cursor()

    sql = "SELECT * from tbl_alunos"
    cursor.execute(sql)

    results = cursor.fetchall()
    if not results:
        resp = {"erro": "Nenhum aluno encontrado"}
        return resp, 404
    else:
        alunos = []
        for aluno in results:
            aluno_dict = {
                "id": aluno[0],
                "nome": aluno[1],
                "email": aluno[2]
            }
            alunos.append(aluno_dict)

        resp = {"alunos": alunos}
        return resp, 200



if __name__ == '__main__':
    app.run(debug=True)
```

Neste exemplo, temos uma API Flask que se conecta a um banco de dados MySQL para obter informações sobre alunos. A rota `/alunos` retorna uma lista de alunos do banco de dados.

## 📌 **Introdução**
Testar APIs Flask é essencial para garantir que as rotas funcionam corretamente e retornam as respostas esperadas. No entanto, como essa API depende de um **banco de dados MySQL**, precisamos garantir que os testes **não dependam de um banco real**.

Para isso, usaremos:

- **pytest** → para rodar os testes.
- **Flask's test client** → para fazer requisições à API durante os testes.
- **Mocks (`unittest.mock`)** → para substituir a conexão real com o banco de dados por um objeto simulado.


## **1️⃣ Configuração do Ambiente de Teste**
Crie um arquivo de testes chamado **`test_api.py`**.


## **2️⃣ Criando o Teste para a Rota `/alunos`**
O objetivo do teste é:

- Simular uma requisição **GET** para `/alunos`.
- Garantir que a API retorna os dados esperados.
- Substituir a conexão com o banco de dados por um **Mock** para que o teste rode sem um banco real.

### **📌 Código do Teste**
```python
import pytest
from unittest.mock import patch, MagicMock
from api import app, connect_db  # Importamos a aplicação Flask e a função de conexão

@pytest.fixture
def client():
    """Cria um cliente de teste para a API."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@patch("api.connect_db")  # Substituímos a função que conecta ao banco por um Mock
def test_get_alunos(mock_connect_db, client):
    """Testa a rota /alunos sem acessar o banco de dados real."""

    # Criamos um Mock para a conexão e o cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    # Configuramos o Mock para retornar o cursor quando chamarmos conn.cursor()
    mock_conn.cursor.return_value = mock_cursor

    # Simulamos o retorno do banco de dados
    mock_cursor.fetchall.return_value = [
        (1, "Alice", "alice@email.com"),
        (2, "Bob", "bob@email.com"),
    ]

    # Substituímos a função `connect_db` para retornar nosso Mock em vez de uma conexão real
    mock_connect_db.return_value = mock_conn

    # Fazemos a requisição para a API
    response = client.get("/alunos")

    # Verificamos se o código de status da resposta é 200 (OK)
    assert response.status_code == 200

    # Verificamos se os dados retornados estão corretos
    expected_response = {
        "alunos": [
            {"id": 1, "nome": "Alice", "email": "alice@email.com"},
            {"id": 2, "nome": "Bob", "email": "bob@email.com"},
        ]
    }
    assert response.get_json() == expected_response

    # Verificamos se a consulta SQL foi executada corretamente
    mock_cursor.execute.assert_called_once_with("SELECT * from tbl_alunos")
```


## **3️⃣ Explicando o Teste**
### 🔹 **1. Criamos um Cliente de Teste**
A fixture `client` cria um **cliente de teste Flask**, que nos permite fazer requisições à API sem precisar rodá-la de verdade.

### 🔹 **2. Usamos um Mock para `connect_db`**
A linha:
```python
@patch("api.connect_db")
```
substitui a função `connect_db()` por um **Mock**, impedindo que a API tente conectar ao banco de dados real.

### 🔹 **3. Criamos uma Conexão e Cursor Falsos**
Usamos **Mocks** para simular o comportamento do banco:
```python
mock_conn = MagicMock()
mock_cursor = MagicMock()
mock_conn.cursor.return_value = mock_cursor
```
Isso significa que sempre que a API chamar `.cursor()`, ela receberá nosso **Mock** em vez de um cursor real.

### 🔹 **4. Simulamos os Dados Retornados pelo Banco**
```python
mock_cursor.fetchall.return_value = [
    (1, "Alice", "alice@email.com"),
    (2, "Bob", "bob@email.com"),
]
```
Isso faz com que a API **pense** que o banco retornou esses valores, permitindo testá-la sem um banco real.

### 🔹 **5. Verificamos a Resposta da API**
Chamamos a rota:
```python
response = client.get("/alunos")
```
E verificamos se:

- O **código de status** é `200 OK`.
- O **JSON retornado** corresponde aos valores simulados.


## **4️⃣ Testando um Caso de Erro (Nenhum Aluno Encontrado)**
Podemos simular um **banco de dados vazio** para testar se a API retorna corretamente o erro `404`.

```python
@patch("api.connect_db")
def test_get_alunos_vazio(mock_connect_db, client):
    """Testa a rota /alunos quando o banco de dados não tem alunos."""

    # Criamos um Mock para a conexão e o cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    # Simulamos que o banco de dados não retorna nenhum aluno
    mock_cursor.fetchall.return_value = []

    mock_connect_db.return_value = mock_conn

    # Fazemos a requisição para a API
    response = client.get("/alunos")

    # Verificamos se o código de status da resposta é 404 (Nenhum aluno encontrado)
    assert response.status_code == 404
    assert response.get_json() == {"erro": "Nenhum aluno encontrado"}
```


## **📌 Resumo**
| **O que fizemos?** | **Por que isso é útil?** |
|--------------------|-------------------------|
| Criamos um **cliente de teste** com Flask | Permite testar a API sem rodá-la de verdade |
| Usamos `patch("api.connect_db")` | Evita que os testes se conectem a um banco real |
| Criamos Mocks para a **conexão e cursor do banco** | Permite simular diferentes respostas da API |
| Testamos a API em diferentes cenários | Garantimos que o código lida bem com dados normais e erros |


## **5️⃣ Executando os Testes**
Agora podemos rodar nossos testes com:

```sh
pytest test_api.py -v
```

Se tudo estiver correto, veremos uma saída como:

```
test_api.py::test_get_alunos PASSED
test_api.py::test_get_alunos_vazio PASSED
```


## **📌 Conclusão**
✅ Aprendemos a testar APIs Flask sem precisar de um banco de dados real.  
✅ Usamos **Mocks** para simular conexões com o banco e diferentes cenários.  
✅ Agora temos testes que garantem que a API funciona corretamente! 🚀  

Isso facilita a **manutenção do código**, garantindo que a API continue funcionando conforme esperado, mesmo com futuras mudanças. 🚀

Agora que você já aprendeu tudo sobre testes automáticos, que tal praticar um pouco mais? Vamos para os [**Exercícios no Prairie Learn**](https://us.prairielearn.com/pl/course_instance/225046){:target="_blank"}!