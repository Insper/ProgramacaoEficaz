# Amadurecendo uma API de Gerenciamento de Tarefas

Responsável: Licia Sales

### **Exercício: Transformando uma API Nível 0 para Nível 2 no Modelo de Maturidade de Richardson**

### **API de Gerenciamento de Tarefas**

Você tem uma API RESTful de gerenciamento de tarefas que atualmente está no nível 0 do modelo de maturidade de Richardson. Isso significa que a API trata todas as interações por meio de um único endpoint, usando métodos HTTP inadequadamente ou sem diferenciação. O objetivo deste exercício é transformar essa API em uma API de nível 2, onde cada recurso tem seu próprio endpoint e os métodos HTTP (GET, POST, PUT, DELETE) são usados de maneira adequada.

**Estrutura da Tarefa:**

- **ID**: Um número inteiro único que identifica a tarefa.
- **Título**: Uma string que representa o título da tarefa.
- **Descrição**: Uma string que fornece mais detalhes sobre a tarefa.
- **Status**: Um valor booleano que indica se a tarefa está concluída (True) ou não (False).

### **Código Nível 0:**

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Estudar para a prova", "description": "Estudar matemática e física", "status": False},
    {"id": 2, "title": "Fazer compras", "description": "Comprar leite e pão", "status": True},
]

@app.route('/api', methods=['POST'])
def handle_requests():
    data = request.json
    action = data.get('action')

    if action == 'get_all':
        return jsonify(tasks)
    elif action == 'get_task':
        task_id = data.get('id')
        task = next((t for t in tasks if t['id'] == task_id), None)
        if task:
            return jsonify(task)
        else:
            return {"error": "Task not found"}, 404
    elif action == 'create_task':
        new_task = {
            "id": len(tasks) + 1,
            "title": data.get('title'),
            "description": data.get('description'),
            "status": data.get('status', False)
        }
        tasks.append(new_task)
        return jsonify(new_task), 201
    elif action == 'update_task':
        task_id = data.get('id')
        task = next((t for t in tasks if t['id'] == task_id), None)
        if task:
            task.update(data)
            return jsonify(task)
        else:
            return {"error": "Task not found"}, 404
    elif action == 'delete_task':
        task_id = data.get('id')
        task = next((t for t in tasks if t['id'] == task_id), None)
        if task:
            tasks.remove(task)
            return {"message": "Task deleted"}, 200
        else:
            return {"error": "Task not found"}, 404

    return {"error": "Invalid action"}, 400

if __name__ == '__main__':
    app.run(debug=True)

```

### **Tarefas do Exercício**

1. **Transformar para Nível 1:**
    - Divida as funcionalidades da API em múltiplos endpoints, cada um representando um recurso específico (como `/tasks`).
    - Exemplo: Crie endpoints separados como `GET /tasks` para listar todas as tarefas, `POST /tasks` para criar uma nova tarefa, etc.
2. **Transformar para Nível 2:**
    - Use os métodos HTTP apropriados para cada operação. Por exemplo, use `GET` para buscar dados, `POST` para criar novos recursos, `PUT` para atualizar recursos e `DELETE` para deletar recursos.
    - Garanta que os endpoints utilizem URLs adequadas que representem os recursos, como `/tasks/<id>` para operações em uma tarefa específica.
3. **Testar a API no Postman:**
    - Após transformar a API para o nível 2, use o Postman para testar cada endpoint. Certifique-se de que os métodos HTTP corretos estão sendo usados e que as URLs seguem as convenções RESTful.