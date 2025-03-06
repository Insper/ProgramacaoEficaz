# Projeto 2

!!! success "Entrega"
    :date: 19/03/2025 (quarta-feira)
    
    :clock1: Commits até as 23:59

    :material-account-group: Duplas

    :simple-github: Entrega via :point_right: [GitHub Classroom](https://classroom.github.com/a/mCuB878M)

## Objetivos :octicons-goal-16:

Durante o primeiro projeto, nós desenvolvemos um servidor capaz de responder com páginas HTML. No segundo projeto, nosso objetivo é desenvolvermos um servidor RESTful que responda com JSON. Para isso, você deve implementar uma API de uma empresa imobiliária.

## Requisitos :octicons-checklist-16:

1. Devem haver rotas para:
    - Listar todos os imóveis com todos os seus atributos;
    - Listar um imóvel específico pelo seu id com todos os seus atributos;
    - Adicionar um novo imóvel;
    - Atualizar um imóvel existente;
    - Remover um imóvel existente;
    - Listar imóveis por tipo (casa, apartamento, terreno, etc) com todos os seus atributos;
    - Listar imóveis por cidade com todos os seus atributos;
1. Devem haver testes automatizados para todas as rotas.
1. O servidor deve ser desenvolvido utilizando o framework Flask.
1. O servidor deve utilizar o banco de dados MySQL hospedado na plataforma Aiven.
1. O projeto deve utilizar os princípios de TDD.
1. O projeto deve ter o deploy feito em um EC2 na AWS.
1. Para gerar o banco de dados, utilize o script disponível [aqui](imoveis.sql)

## Rubrica :material-check:

A rubrica a seguir será utilizada na correção do Projeto 2:

Para que a nota seja considerada, é necessário possuir contribuições em seu nome no repositório do projeto. Caso esteja em dupla, é necessário que ambos tenham contribuições.

Se os dois membros da dupla estiverem trabalhando no mesmo código juntos, faça o commit utilizando o comando de coautores como mostrado [aqui](../../auxiliar/coautores.md).

| Conceito | Descrição |
| :------: | :-------- |
|    I     | Não entregou ou o código não executa |
|    D     | Criou o código do servidor antes dos testes, ou não foram feitas corretamente as rotas solicitadas. |
|    C     | Criou os testes antes do código do servidor, mas não utilizou corretamente todos os princípios de TDD vistos. Todas as rotas respondem corretamente mas a API não é RESTful.  |
|    C+    | No geral aplicou corretamente os princípios de TDD e a API é RESTful, mas houveram alguns pequenos erros. |
|    B     | Aplicou corretamente os princípios de TDD, a API é RESTful e se comunica com um banco de dados MySQL hospedado no Aiven. A API está no nível 2 da Maturidade de Richardson |
|    B+    | Atingiu o conceito B e o projeto está hospedado e acessível na AWS. Há um link para o serviço no arquivo README do projeto. |
|    A     | Atingiu o conceito B+ e a API retorna os códigos HTTP corretos para a ação executada, como descritos [aqui](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status). |
|    A+     | Atingiu o conceito A e a API está no nível 3 da Maturidade de Richardson. |