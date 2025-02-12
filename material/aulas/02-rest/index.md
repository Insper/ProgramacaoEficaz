# O que é REST

Responsável: Andre Oliveira

**Referências:**

- [https://developer.mozilla.org/pt-BR/docs/Glossary/REST](https://developer.mozilla.org/pt-BR/docs/Glossary/REST)

- **“REST** (Representational State Transfer) refere-se a um grupo de restrições de design dentro da arquitetura de software que geram sistemas distribuídos eficientes, confiáveis e escaláveis. Um sistema é denominado RESTful quando adere a todas essas restrições.”

- “A ideia básica do REST é que um recurso, por exemplo um documento, seja transferido com seu estado bem definido, padronização de operações e formatos.”

- **Recurso** ⇒ “Um recurso é um elemento abstrato e que nos permite mapear qualquer coisa do mundo real como um elemento para acesso via Web.”

- Uso explicito dos verbos HTTP
    - GET ⇒ Buscar/Pegar informações de um recurso especificado na url da requisição (ex: /itens)
    - POST ⇒ Criar um recurso especificado na url da requisição (ex: /itens)
    - DELETE ⇒ Deleta um recurso especificado na url da requisição (ex: /itens/<id>)
    - PUT ⇒ Atualiza um recurso especificado na url da requisição (ex: /itens/<id>)
    
    ```python
    # Código gerado com o ChatGPT
    from flask import Flask, jsonify, request
    
    app = Flask(__name__)
    
    # Representação do banco de dados 
    tasks = [
        {"id": 1, "title": "Estudar Python", "done": False},
        {"id": 2, "title": "Fazer compras", "done": True}
    ]
    
    # Observe como que os recursos são representados dentro da URL de requisição, ou seja, apenas lendo o caminho do recurso + seu verbo HTTP é possível ter uma ideia do que essa rota deve retornar e fazer
    @app.route('/tasks', methods=['GET'])
    def get_tasks():
        return jsonify({"tasks": tasks})
    
    @app.route('/tasks/<int:task_id>', methods=['GET'])
    def get_task(task_id):
        task = next((task for task in tasks if task['id'] == task_id), None)
        if task:
            return jsonify({"task": task})
        else:
            return jsonify({"message": "Tarefa não encontrada"}), 404
    
    @app.route('/tasks', methods=['POST'])
    def create_task():
        new_task = request.json
        tasks.append(new_task)
        return jsonify({"message": "Tarefa criada com sucesso"}), 201
    
    @app.route('/tasks/<int:task_id>', methods=['PUT'])
    def update_task(task_id):
        task = next((task for task in tasks if task['id'] == task_id), None)
        if task:
            task.update(request.json)
            return jsonify({"message": "Tarefa atualizada com sucesso"})
        else:
            return jsonify({"message": "Tarefa não encontrada"}), 404
    
    @app.route('/tasks/<int:task_id>', methods=['DELETE'])
    def delete_task(task_id):
        tasks = [task for task in tasks if task['id'] != task_id]
        return jsonify({"message": "Tarefa excluída com sucesso"})
    
    if __name__ == '__main__':
        app.run(debug=True)
    
    ```
    

- **Stateless** ⇒ “Não é armazenado nenhum estado no servidor.” Não dependem de dados armazenados de outra requisição para poder executar a requisição atual. Todos os dados necessários para requisição se completar devem ser enviados e armazenados pelo cliente

- **Representação** ⇒ JSON - *Os dados normalmente chegam e retornam em JSON*

- **Respostas HTTP** coerentes com o estado da requisição:
    - Referencia para consulta das respostas: 
    [https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status)