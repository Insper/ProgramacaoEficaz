# Aplicação de Gerenciamento de Livros

Responsável: Licia Sales

Você está desenvolvendo uma API RESTful para gerenciar o acervo de livros de uma biblioteca. O objetivo é permitir que os bibliotecários possam adicionar novos livros, visualizar detalhes de livros existentes, atualizar informações e remover livros do acervo. Cada livro terá um identificador único, um título, um autor e um status indicando se o livro está disponível ou emprestado.

**Estrutura do Livro:**

- **ID**: Um número inteiro único que identifica o livro.
- **Título**: Uma string que representa o título do livro.
- **Autor**: Uma string que representa o autor do livro.
- **Status**: Uma string que indica se o livro está "Disponível" ou "Emprestado".

**Exemplo de Dados Iniciais:**

```python
books = [
    {
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "status": "Disponível"
    },
    {
        "id": 2,
        "title": "Dom Casmurro",
        "author": "Machado de Assis",
        "status": "Emprestado"
    },
    {
        "id": 3,
        "title": "A Revolução dos Bichos",
        "author": "George Orwell",
        "status": "Disponível"
    }
]

```

### 

1. **GET /books**: Retorna a lista de todos os livros no acervo.
2. **POST /books**: Adiciona um novo livro ao acervo.
3. **GET /books/<id>**: Retorna um livro específico pelo ID.
4. **PUT /books/<id>**: Atualiza as informações de um livro específico.
5. **DELETE /books/<id>**: Remove um livro específico do acervo.

### **Instruções:**

1. **Implementar os Endpoints:** Com base na estrutura de dados fornecida e utilizando o Flask, crie os endpoints para as operações listadas.
2. **Testar os Endpoints no Postman:** Após implementar cada endpoint, use o Postman para enviar requisições e verificar se estão funcionando corretamente. Certifique-se de testar cenários de sucesso e erro, como tentar atualizar o status de um livro que não existe.
3. **Refinar o Código:** Após os testes, faça ajustes no código conforme necessário para lidar com possíveis erros e garantir que o serviço esteja robusto.

**Resultado Esperado:** Um serviço web funcional que permite a manipulação completa do acervo de livros, operando corretamente com as requisições testadas no Postman.