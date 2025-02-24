# Corrigindo Erros em uma API de Gerenciamento de Pedidos de Restaurante

Responsável: Licia Sales

Você recebeu uma API RESTful para o gerenciamento de pedidos em um restaurante, que já foi desenvolvida, mas contém alguns erros que precisam ser corrigidos. A API deve permitir criar novos pedidos, visualizar pedidos existentes, atualizar o status dos pedidos e remover pedidos. Cada pedido tem um identificador único, o nome do cliente, os itens do pedido e o status (ex: "Em preparo", "Pronto", "Entregue").

**Estrutura do Pedido:**

- **ID**: Um número inteiro único que identifica o pedido.
- **Nome do Cliente**: Uma string que representa o nome do cliente.
- **Itens**: Uma lista de strings que descreve os itens do pedido.
- **Status**: Uma string que representa o status do pedido.

### **Código bugado:**

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de pedidos de exemplo
orders = [
    {"id": 1, "customer_name": "João Silva", "items": ["Pizza", "Refrigerante"], "status": "Em preparo"},
    {"id": 2, "customer_name": "Maria Oliveira", "items": ["Hambúrguer", "Batata Frita"], "status": "Pronto"},
]

@app.route('/orders', methods=['GET'])
def get_orders():
    if len(orders) == 0:
        return {"error": "No orders found"}  
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def add_order():
    new_order = request.json
    if not new_order["customer_name"] or not new_order["items"]:
        return {"error": "Invalid data"}, 400  
    new_order["id"] = len(orders) + 1
    orders.append(new_order)
    return jsonify(new_order), 201

@app.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    for order in orders:
        if order["id"] == id:
            return order  
    return {"error": "Order not found"}, 404

@app.route('/orders/<int:id>', methods=['PUT'])
def update_order(id):
    updated_order = request.json
    for order in orders:
        if order["id"] == id:
            order.update(updated_order)  
            return jsonify(order)
    return {"error": "Order not found"}, 404

@app.route('/orders/<int:id>', methods=['DELETE'])
def delete_order(id):
    for order in orders:
        if order["id"] == id:
            orders.remove(order)
            return {"message": "Order deleted"}, 200
    return {"error": "Order not found"}, 404

if __name__ == '__main__':
    app.run(debug=True)

```

### **Testar a API no Postman:**

- Após corrigir os erros, use o Postman para testar cada endpoint. Eles devem garantir que todas as operações funcionem conforme o esperado, incluindo cenários de sucesso e falha.

### **Dica sobre os bugs no exercício:**
---

- **Dica 1:** Verifique se o endpoint `GET /orders` está retornando a informação no formato JSON e lidando corretamente quando não há pedidos.
- **Dica 2:** Verifique se o endpoint `POST /orders` está validando corretamente todos os campos obrigatórios antes de criar um novo pedido.
- **Dica 3:** Verifique se o endpoint `GET /orders/<id>` está retornando a resposta no formato JSON e tratando adequadamente pedidos que não existem.
- **Dica 4:** Verifique se o endpoint `PUT /orders/<id>` permite a atualização parcial dos dados do pedido, preservando os dados que não foram enviados.
- **Dica 5:** Verifique se o endpoint `DELETE /orders/<id>` remove corretamente o pedido e verifica se o pedido existe.