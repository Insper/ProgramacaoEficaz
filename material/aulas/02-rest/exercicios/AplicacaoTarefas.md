# Aplicação de Gerenciamento de Tarefas

Responsável: Licia Sales

Você foi contratado para desenvolver o backend de uma API RESTful para gerenciar uma lista de tarefas diárias. O objetivo é permitir que os usuários possam criar, visualizar, atualizar e excluir tarefas de maneira fácil e rápida. Cada tarefa terá um identificador único, um título, uma descrição e um status que indica se a tarefa foi concluída ou não.

**Estrutura da Tarefa:**

- **ID**: Um número inteiro único que identifica a tarefa.
- **Título**: Uma string que descreve o título da tarefa.
- **Descrição**: Uma string que fornece mais detalhes sobre a tarefa.
- **Status**: Um valor booleano que indica se a tarefa está concluída (True) ou não (False).

**Exemplo de Dados Iniciais:**

```python
tasks = [
    {
        "id": 1,
        "title": "Estudar Python",
        "description": "Ler o capítulo sobre Flask e APIs RESTful",
        "status": False
    },
    {
        "id": 2,
        "title": "Comprar comida",
        "description": "comprar frutas e vegetais para a semana",
        "status": False
    },
    {
        "id": 3,
        "title": "Passear com o pet",
        "description": "Caminhar por 30 minutos no parque",
        "status": True
    }
]

```

1. **GET /tarefa**: Retorna a lista de todas as tarefas.
2. **POST /tarefa**: Adiciona uma nova tarefa.
3. **GET /tasks/<id>**: Retorna uma tarefa específica pelo ID.
4. **PUT /tasks/<id>**: Atualiza uma tarefa específica.
5. **DELETE /tasks/<id>**: Deleta uma tarefa específica.

### **Instruções:**

1. **Implementar os Endpoints:** Com base na estrutura de dados fornecida e utilizando o Flask, crie os endpoints para as operações listadas.
2. **Testar os Endpoints no Postman:** Após implementar cada endpoint, use o Postman para enviar requisições e verificar se estão funcionando corretamente. Certifique-se de testar todos os cenários, incluindo erros (por exemplo, tentar acessar uma tarefa com um ID que não existe).
3. **Refinar o Código:** Após os testes, faça ajustes no código conforme necessário para lidar com possíveis erros e garantir que o serviço esteja robusto.

**Resultado Esperado:** Um serviço web funcional que permite a manipulação completa da lista de tarefas, operando corretamente com as requisições testadas no Postman.