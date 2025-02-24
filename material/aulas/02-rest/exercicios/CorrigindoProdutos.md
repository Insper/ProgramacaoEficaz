# Corrigindo Erros em uma API de Gerenciamento de Produtos

Responsável: Licia Sales

### **API de Gerenciamento de Produtos**

Você recebeu uma API RESTful de gerenciamento de produtos que já foi desenvolvida, mas contém alguns erros que precisam ser corrigidos. A API deve permitir adicionar novos produtos, visualizar produtos existentes, atualizar detalhes de produtos e remover produtos. Cada produto tem um identificador único, um nome, uma descrição e um preço.

**Estrutura do Produto:**

- **ID**: Um número inteiro único que identifica o produto.
- **Nome**: Uma string que representa o nome do produto.
- **Descrição**: Uma string que descreve o produto.
- **Preço**: Um número de ponto flutuante que representa o preço do produto.

### **Código bugado:**

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de produtos de exemplo
products = [
    {"id": 1, "name": "Laptop", "description": "Um laptop poderoso", "price": 1500.00},
    {"id": 2, "name": "Mouse", "description": "Mouse sem fio", "price": 50.00},
]

@app.route('/products', methods=['GET'])
def get_products():
    return products  

@app.route('/products', methods=['POST'])
def add_product():
    new_product = request.json
    products.append(new_product)
    return jsonify(new_product), 201

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    for product in products:
        if product["id"] == id:
            return product  
    return {"error": "Product not found"}, 404

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    updated_product = request.json
    for product in products:
        if product["id"] == id:
            product = updated_product  
            return jsonify(product)
    return {"error": "Product not found"}, 404

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    for product in products:
        if product["id"] == id:
            products.remove(product)
            return {"message": "Product deleted"}, 200
    return {"error": "Product not found"}, 404

if __name__ == '__main__':
    app.run(debug=True)

```

### **Testar a API no Postman:**

- Após corrigir os erros, use o Postman para testar cada endpoint. Eles devem garantir que todas as operações funcionem conforme o esperado, incluindo cenários de sucesso e falha.

### **Dica sobre os bugs no exercicio:**

---

- **Dica 1:** Verifique se o endpoint `GET /products` está retornando a informação no formato JSON.
- **Dica 2:** Verifique se o endpoint `POST /products` está validando todos os campos antes de adicionar um novo produto.
- **Dica 3:** Verifique se o endpoint `GET /products/<id>` está retornando a resposta no formato JSON. Além disso, verifique se o código está tratando possíveis requisições com IDs que não existem.
- **Dica 4:** Verifique se o endpoint `PUT /products/<id>` permite a atualização parcial dos dados do produto, sem substituir o produto inteiro.
- **Dica 5:** Verifique se o endpoint `DELETE /products/<id>`  remove corretamente o produto e verifica se o produto existe.