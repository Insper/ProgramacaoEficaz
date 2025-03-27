# Migração de MySQL para MongoDB com Flask e PyMongo

## Principais Mudanças

| Aspecto                  | MySQL                              | MongoDB (com PyMongo)               |
|--------------------------|-------------------------------------|--------------------------------------|
| Biblioteca de acesso     | `mysql.connector`                  | `pymongo`                             |
| Conexão                  | Config dict com host, user, etc.   | URI (`mongodb://...`)                |
| Consulta de dados        | `cursor.execute` + `fetchall()`    | `collection.find()`                  |
| Tabelas vs. Coleções     | `tbl_alunos` (tabela)              | `alunos` (coleção)                   |
| Formato de retorno       | Tuplas                             | Documentos/dicionários               |
| Esquema rígido           | Sim                                | Não (flexível)                       |

Para fazer a migração de um projeto de MySQL para MongoDB, é necessário adaptar o código para usar a biblioteca `pymongo` e ajustar as consultas e operações de banco de dados. Abaixo está o mesmo exemplo que utilizamos para o MySQL, mas agora utilizando o MongoDB com a biblioteca `pymongo`.

## Exemplo de Código

```python
from flask import Flask, request
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv('.cred')

mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
db_name = os.getenv('DB_NAME', 'db_escola')

def connect_db():
    try:
        client = MongoClient(mongo_uri)
        db = client[db_name]
        return db
    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")
        return None

app = Flask(__name__)

@app.route('/alunos', methods=['GET'])
def get_alunos():
    db = connect_db()
    if db is None:
        return {"erro": "Erro ao conectar ao banco de dados"}, 500

    try:
        collection = db['alunos']
        alunos_cursor = collection.find({}, {"_id": 0})  # Remove o campo _id da resposta
        alunos = list(alunos_cursor)

        if not alunos:
            return {"erro": "Nenhum aluno encontrado"}, 404
        return {"alunos": alunos}, 200
    except Exception as e:
        return {"erro": f"Erro ao consultar alunos: {str(e)}"}, 500

if __name__ == '__main__':
    app.run(debug=True)
```

## Exemplo de testes

Assim como no MySQL, podemos criar testes automatizados para verificar se a API está funcionando corretamente. Abaixo estão um exemplo de teste utilizando a biblioteca `pytest`.

```python
import pytest
from unittest.mock import patch, MagicMock
from api import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@patch("api.connect_db")
def test_get_alunos(mock_connect_db, client):
    mock_collection = MagicMock()
    mock_collection.find.return_value = [
        {"id": 1, "nome": "Alice", "email": "alice@email.com"},
        {"id": 2, "nome": "Bob", "email": "bob@email.com"},
    ]

    mock_db = MagicMock()
    mock_db.__getitem__.return_value = mock_collection
    mock_connect_db.return_value = mock_db

    response = client.get("/alunos")

    assert response.status_code == 200
    assert response.get_json() == {
        "alunos": [
            {"id": 1, "nome": "Alice", "email": "alice@email.com"},
            {"id": 2, "nome": "Bob", "email": "bob@email.com"},
        ]
    }
```