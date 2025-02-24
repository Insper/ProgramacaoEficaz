# Amadurecendo uma API de Gerenciamento de Eventos

Responsável: Licia Sales

### **Exercício: Transformando uma API Nível 0 para Nível 2 no Modelo de Maturidade de Richardson**

### **API de Gerenciamento de Eventos**

Você tem uma API RESTful para o gerenciamento de eventos que atualmente está no nível 0 do modelo de maturidade de Richardson. Isso significa que todas as operações da API são tratadas por meio de um único endpoint, sem uso adequado dos métodos HTTP e sem diferenciação de recursos. O objetivo deste exercício é transformar essa API em uma API de nível 2, onde cada recurso tem seu próprio endpoint, e os métodos HTTP (GET, POST, PUT, DELETE) são usados corretamente.

**Estrutura do Evento:**

- **ID**: Um número inteiro único que identifica o evento.
- **Nome**: Uma string que representa o nome do evento.
- **Data**: Uma string que representa a data do evento no formato YYYY-MM-DD.
- **Local**: Uma string que descreve o local onde o evento será realizado.

### **Código Nível 0:**

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

events = [
    {"id": 1, "name": "Conferência de Tecnologia", "date": "2023-11-10", "location": "Centro de Convenções"},
    {"id": 2, "name": "Workshop de Design", "date": "2023-12-05", "location": "Sala de Conferências A"},
]

@app.route('/api', methods=['POST'])
def handle_requests():
    data = request.json
    action = data.get('action')

    if action == 'get_all_events':
        return jsonify(events)
    elif action == 'get_event':
        event_id = data.get('id')
        event = next((e for e in events if e['id'] == event_id), None)
        if event:
            return jsonify(event)
        else:
            return {"error": "Event not found"}, 404
    elif action == 'create_event':
        new_event = {
            "id": len(events) + 1,
            "name": data.get('name'),
            "date": data.get('date'),
            "location": data.get('location')
        }
        events.append(new_event)
        return jsonify(new_event), 201
    elif action == 'update_event':
        event_id = data.get('id')
        event = next((e for e in events if e['id'] == event_id), None)
        if event:
            event.update(data)
            return jsonify(event)
        else:
            return {"error": "Event not found"}, 404
    elif action == 'delete_event':
        event_id = data.get('id')
        event = next((e for e in events if e['id'] == event_id), None)
        if event:
            events.remove(event)
            return {"message": "Event deleted"}, 200
        else:
            return {"error": "Event not found"}, 404

    return {"error": "Invalid action"}, 400

if __name__ == '__main__':
    app.run(debug=True)

```

### **Tarefas do Exercício**

1. **Transformar para Nível 1:**
    - Separe as funcionalidades da API em múltiplos endpoints, cada um representando um recurso específico, como `/events` para o recurso de eventos.
    - Exemplo: Crie endpoints separados como `GET /events` para listar todos os eventos, `POST /events` para adicionar um novo evento, etc.
2. **Transformar para Nível 2:**
    - Utilize os métodos HTTP adequados para cada operação. Por exemplo, use `GET` para buscar eventos, `POST` para adicionar novos eventos, `PUT` para atualizar eventos e `DELETE` para remover eventos.
    - As URLs dos endpoints devem refletir corretamente os recursos, como `/events/<id>` para operações em um evento específico.
3. **Testar a API no Postman:**
    - Após transformar a API para o nível 2, use o Postman para testar cada endpoint. Certifique-se de que os métodos HTTP corretos estão sendo usados e que as URLs seguem as convenções RESTful.