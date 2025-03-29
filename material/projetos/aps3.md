# APS 3

!!! success "Entrega"
    :date: 25/04 (sexta-feira)
    
    :clock1: até as 23:59

    :material-account-group: Individual

    :simple-github: Entrega via :point_right: Blackboard.
 
Para completar esta APS os seguintes links serão bastante úteis:

- W3 Schools ([https://www.w3schools.com/mongodb/](https://www.w3schools.com/mongodb/))
- Cheat Sheet do MongoDB ([https://www.mongodb.com/developer/products/mongodb/cheat-sheet/](https://www.mongodb.com/developer/products/mongodb/cheat-sheet/))
- Documentação do MongoDB ([https://www.mongodb.com/pt-br/docs/manual/reference/operator/query/](https://www.mongodb.com/pt-br/docs/manual/reference/operator/query/))


## O que você precisa saber e fazer antes de iniciar os exercícios

- A entrega dos exercícios deve ser enviada em PDF pelo Blackboard com texto gerado em LaTeX, usando o template disponível em [https://www.overleaf.com/read/zgybjvrygnfw#19e451](https://www.overleaf.com/read/zgybjvrygnfw#19e451)

- Faça o download dos arquivos [`livros.json`](aps3/livros.json) e [`usuarios.json`](aps3/usuarios.json). Esses arquivos contém dados completamente inventados e não validos, apenas para fins de teste.

- Crie um banco de dados no MongoDB Atlas como instruído [aqui](../aulas/mongo/configuracao.md).

- Se conecte ao banco de dados utilizando o MongoDB Compass.

- Crie um banco de dados chamado `biblioteca`. Para isso:
    - Clique em `+ Create Database`
    - No campo `Database Name` coloque `biblioteca`
    - No campo `Collection Name` coloque `livros`

- Importe os livros:
    - Acesse o banco `biblioteca`.
    - Clique na coleção `livros`.
    - Clique em `Add Data` e depois em `Import JSON`.
    - Escolha o arquivo `livros.json`.
    - Clique em `Import`.

- Importe os usuários:
    - Clique no botão `+` ao lado do nome do banco de dados `biblioteca` e crie uma nova coleção chamada `usuarios`.
    - Clique na coleção `usuarios`.
    - Clique em `Add Data` e depois em `Import JSON`.
    - Escolha o arquivo `usuarios.json`.
    - Clique em `Import`.

- Clique no botão `Open MongoDB shell` no canto superior direito para abrir o terminal do MongoDB.
- Execute o seguinte comando para verificar se os dados foram importados corretamente:

```javascript
use biblioteca
db.usuarios.find().pretty()
```

Caso o comando acima retorne os dados dos usuários, a importação foi realizada com sucesso.

## Como será a avaliação?

O feedback referente a esta atividade será disponibilizado a todos os alunos, indicando as questões corretas e incorretas incluindo as sugestões para melhoria. O conceito na atividade será atribuído pelo número de questões corretas, como segue a Tabela abaixo:

| Conceito | Número de Acertos |
| :------: | :-------- |
|    I     | 0 |
|    D     | 2 |
|    C     | 4 |
|    C+    | 6 |
|    B     | 8 |
|    B+    | 9 |
|    A     | 10 |
|    A+    | 11 |

**Reforçamos que não serão aceitos exercícios entregues fora do prazo e que na entrega não realizada será atribuído conceito I**

## Exercícios

Os exercícios consistem em realizar consultas no banco de dados `biblioteca` que você criou e importou os dados em formato `MongoDB Shell Syntax`. Para isso, teste as consultas utilizando o shell do MongoDB Compass.

1. Liste todos os livros disponíveis.
1. Busque todos os livros do autor "Machado de Assis".
1. Atualizar a disponibilidade de "Poemas para um Mundo Novo 5" para `false`.
1. Apague da coleção `livros` todos os livros publicados antes de 1900.
1. Insira um novo livro na coleção `livros` com os seguintes dados:
    - Título: "O Pequeno Príncipe"
    - Autor: "Antoine de Saint-Exupéry"
    - Ano de Publicação: 1943
    - Disponibilidade: `true`
1. Insira com um único comando três novos livros na coleção `livros` com os seguintes dados:
    - Livro 1:
        - Título: "1984"
        - Autor: "George Orwell"
        - Ano de Publicação: 1949
        - Disponibilidade: `true`
    - Livro 2:
        - Título: "A Revolução dos Bichos"
        - Autor: "George Orwell"
        - Ano de Publicação: 1945
        - Disponibilidade: `true`
    - Livro 3:
        - Título: "O Senhor dos Anéis"
        - Autor: "J.R.R. Tolkien"
        - Ano de Publicação: 1954
        - Disponibilidade: `true`
1. Adicione o empréstimo do livro "A Revolução dos Bichos" para a usuária "Ana".
1. Liste os usuários que têm pelo menos um livro emprestado.
1. Busque a usuária "Ana" e mostre seu nome e o título dos livros que ela possui emprestados. A resposta deve ser como a abaixo:

    ```
    {
        nome: 'Ana',
        livros_emprestados: [
            {
                titulo: 'Poemas para um Mundo Novo 11'
            },
            {
                titulo: 'Mistérios de Pedra 1'
            },
            {
                titulo: 'O Vento e as Estrelas 9'
            },
            {
                titulo: 'A Revolução dos Bichos'
            }
        ]
    }
    ```

1. Liste os usuários que tenham pego emprestado o livro "Mistérios de Pedra 1".
1. Liste o título de todos os livros que já foram emprestados sem repetição.