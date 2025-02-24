# Corrigindo Erros em uma API de Gerenciamento de Usuários

Responsável: Licia Sales

Você recebeu uma API RESTful de gerenciamento de usuários que já foi desenvolvida, mas contém alguns erros que precisam ser corrigidos. A API deve permitir adicionar novos usuários, visualizar usuários existentes, atualizar detalhes dos usuários e remover usuários. Cada usuário tem um identificador único, um nome, um e-mail e uma idade.

**Estrutura do Usuário:**

- **ID**: Um número inteiro único que identifica o usuário.
- **Nome**: Uma string que representa o nome do usuário.
- **E-mail**: Uma string que representa o endereço de e-mail do usuário.
- **Idade**: Um número inteiro que representa a idade do usuário.

### **Código bugado:**

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de usuários de exemplo
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 30},
    {"id": 2, "name": "Bob", "email": "bob@example.com", "age": 25},
]

@app.route('/users', methods=['GET'])
def get_users():
    return users  

@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.json
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    for user in users:
        if user["id"] == id:
            return user 
    return {"error": "User not found"}, 404

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    updated_user = request.json
    for user in users:
        if user["id"] == id:
            user = updated_user 
            return jsonify(user)
    return {"error": "User not found"}, 404

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    for user in users:
        if user["id"] == id:
            users.remove(user)
            return {"message": "User deleted"}, 200
    return {"error": "User not found"}, 404

if __name__ == '__main__':
    app.run(debug=True)

```

### **Testar a API no Postman:**

- Após corrigir os erros, use o Postman para testar cada endpoint. Eles devem garantir que todas as operações funcionem conforme o esperado, incluindo cenários de sucesso e falha.

### **Dica sobre os bugs no exercício:**
---
- **Dica 1:** Verifique se o endpoint `GET /users` está retornando a informação no formato JSON.
- **Dica 2:** Verifique se o endpoint `POST /users` está validando todos os campos antes de adicionar um novo usuário.
- **Dica 3:** Verifique se o endpoint `GET /users/<id>` está retornando a resposta no formato JSON. Além disso, verifique se o código está tratando possíveis requisições com IDs que não existem.
- **Dica 4:** Verifique se o endpoint `PUT /users/<id>` permite a atualização parcial dos dados do usuário, sem substituir o usuário inteiro.
- **Dica 5:** Verifique se o endpoint `DELETE /users/<id>` remove corretamente o usuário e verifica se o usuário existe.