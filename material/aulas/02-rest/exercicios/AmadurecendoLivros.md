# Amadurecendo uma API de Gerenciamento de Livros

Responsável: Licia Sales

### **Exercício: Transformando uma API Nível 0 para Nível 2 no Modelo de Maturidade de Richardson**

### **API de Gerenciamento de Livros**

Você tem uma API RESTful de gerenciamento de livros que atualmente está no nível 0 do modelo de maturidade de Richardson. Isso significa que a API usa um único endpoint para todas as operações e não faz uso adequado dos métodos HTTP. O objetivo deste exercício é transformar essa API em uma API de nível 2, onde cada recurso (livro) tem seu próprio endpoint, e os métodos HTTP (GET, POST, PUT, DELETE) são usados corretamente.

**Estrutura do Livro:**

- **ID**: Um número inteiro único que identifica o livro.
- **Título**: Uma string que representa o título do livro.
- **Autor**: Uma string que representa o autor do livro.
- **Status**: Uma string que indica se o livro está "Disponível" ou "Emprestado".

### **Código Nível 0:**

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "status": "Disponível"},
    {"id": 2, "title": "Dom Casmurro", "author": "Machado de Assis", "status": "Emprestado"},
]

@app.route('/api/books', methods=['POST'])
def handle_books():
    data = request.json
    action = data.get('action')

    if action == 'get_all':
        return jsonify(books)
    elif action == 'get_book':
        book_id = data.get('id')
        book = next((b for b in books if b['id'] == book_id), None)
        if book:
            return jsonify(book)
        else:
            return {"error": "Book not found"}, 404
    elif action == 'add_book':
        new_book = {
            "id": len(books) + 1,
            "title": data.get('title'),
            "author": data.get('author'),
            "status": data.get('status', "Disponível")
        }
        books.append(new_book)
        return jsonify(new_book), 201
    elif action == 'update_book':
        book_id = data.get('id')
        book = next((b for b in books if b['id'] == book_id), None)
        if book:
            book.update(data)
            return jsonify(book)
        else:
            return {"error": "Book not found"}, 404
    elif action == 'delete_book':
        book_id = data.get('id')
        book = next((b for b in books if b['id'] == book_id), None)
        if book:
            books.remove(book)
            return {"message": "Book deleted"}, 200
        else:
            return {"error": "Book not found"}, 404

    return {"error": "Invalid action"}, 400

if __name__ == '__main__':
    app.run(debug=True)

```

### **Tarefas do Exercício**

1. **Transformar para Nível 1:**
    - Separe as funcionalidades da API em múltiplos endpoints, cada um representando um recurso específico, como `/books`.
    - Exemplo: Crie endpoints separados como `GET /books` para listar todos os livros, `POST /books` para adicionar um novo livro, etc.
2. **Transformar para Nível 2:**
    - Use os métodos HTTP adequados para cada operação. Por exemplo, use `GET` para recuperar dados, `POST` para criar novos recursos, `PUT` para atualizar recursos e `DELETE` para deletar recursos.
    - Garanta que os endpoints usem URLs que representem corretamente os recursos, como `/books/<id>` para operações em um livro específico.
3. **Testar a API no Postman:**
    - Após transformar a API para o nível 2, use o Postman para testar cada endpoint. Verifique se os métodos HTTP corretos estão sendo usados e se as URLs seguem as convenções RESTful.