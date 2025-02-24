# Aplicação de Gerenciamento de Contatos

Responsável: Licia Sales

Você está desenvolvendo uma API RESTful para gerenciar contatos pessoais. O objetivo é permitir que os usuários possam criar, visualizar, atualizar e excluir contatos da sua lista de contatos. Cada contato terá um identificador único, um nome, um e-mail, e um número de telefone.

**Estrutura do Contato:**

- **ID**: Um número inteiro único que identifica o contato.
- **Nome**: Uma string que representa o nome completo do contato.
- **E-mail**: Uma string que contém o endereço de e-mail do contato.
- **Telefone**: Uma string que contém o número de telefone do contato.

**Exemplo de Dados Iniciais:**

```python
contacts = [
    {
        "id": 1,
        "name": "Alice Souza",
        "email": "alice.souza@example.com",
        "phone": "11987654321"
    },
    {
        "id": 2,
        "name": "Bruno Carvalho",
        "email": "bruno.carvalho@example.com",
        "phone": "11998765432"
    },
    {
        "id": 3,
        "name": "Carlos Almeida",
        "email": "carlos.almeida@example.com",
        "phone": "21987654321"
    }
]

```

### 

1. **GET /contacts**: Retorna a lista de todos os contatos.
2. **POST /contacts**: Adiciona um novo contato.
3. **GET /contacts/<id>**: Retorna um contato específico pelo ID.
4. **PUT /contacts/<id>**: Atualiza um contato específico.
5. **DELETE /contacts/<id>**: Deleta um contato específico.

### **Instruções:**

1. **Implementar os Endpoints:** Com base na estrutura de dados fornecida e utilizando o Flask, crie os endpoints para as operações listadas.
2. **Testar os Endpoints no Postman:** Após implementar cada endpoint, use o Postman para enviar requisições e verificar se estão funcionando corretamente. Teste também cenários de erro, como tentar acessar um contato que não existe.
3. **Refinar o Código:** Após os testes, faça ajustes no código conforme necessário para lidar com possíveis erros e garantir que o serviço esteja robusto.

**Resultado Esperado:** Um serviço web funcional que permite a manipulação completa da lista de contatos, operando corretamente com as requisições testadas no Postman.