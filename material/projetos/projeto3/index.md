# Projeto Final

!!! success "Entrega"
    :date: 07/05/2025 (quarta-feira)
    
    :clock1: Commits até as 23:59

    :material-account-group: Mesmos grupos de Projeto Ágil + no máximo 1 aluno que não esteja cursando a disciplina.

    :simple-github: Entrega via :point_right: GitHub Classroom.

## Objetivos :octicons-goal-16:

Neste projeto, o objetivo é criar dois softwares que se comuniquem entre si. O primeiro software é um servidor RESTful Flask que deve ser capaz de receber requisições HTTP e retornar respostas em formato JSON. O segundo software é um cliente em React que deve ser capaz de enviar requisições HTTP para o servidor e processar as respostas.

## Requisitos :octicons-checklist-16:

1. O servidor deve ser desenvolvido utilizando o framework Flask.
1. O servidor deve estar em conformidade com os princípios REST estando no nível 2 da Maturidade de Richardson.
1. O servidor deve utilizar o banco de dados MongoDB hospedado na plataforma Atlas.
1. O cliente deve ser desenvolvido utilizando o framework React.
1. O cliente deve ser capaz de enviar requisições HTTP para o servidor e processar as respostas.
1. O projeto deve ter o deploy feito em um EC2 na AWS.
1. O tema do projeto deve ser escolhido pelo grupo, mas deve ser validado pelo professor.
1. O projeto deve utilizar-se de pelo menos uma API externa.
1. O código do servidor deve estar no seguinte GitHub Classroom: [link](https://classroom.github.com/a/3BoLKVKL){:target=_blank}.
1. O código do cliente deve estar no seguinte GitHub Classroom: [link](https://classroom.github.com/a/D5wGlXsp){:target=_blank}.
1. Os arquivos de credenciais não devem ser commitados nos repositórios. Utilize variáveis de ambiente para armazenar as credenciais. Os arquivos de credenciais devem ser enviados via Blackboard para permitir a correção.

## Rubrica :material-check:

A rubrica a seguir será utilizada na correção do Projeto Final:

Para que a nota seja considerada, é necessário possuir contribuições em seu nome nos repositórios do projeto.

Se mais de um membro do grupo estiver trabalhando no mesmo código, faça o commit utilizando o comando de coautores como mostrado [aqui](../../auxiliar/coautores.md).

| Conceito | Descrição |
| :------: | :-------- |
|    I     | Não entregou ou o código não executa |
|    D     | A API não é RESTful, ou não se conecta a um banco MongoDB no Atlas ou o cliente React não se conecta corretamente na API. |
|    C     | A API é RESTful. O cliente React se conecta com a API. Algumas telas apresentam erro quando utilizadas ou não foi utilizada uma API externa. |
|    C+    | A API é RESTful e se comunica com um banco de dados MongoDB hospedado no Atlas. A API está no nível 2 da Maturidade de Richardson. O cliente React se conecta com a API e consegue acessar e manipular corretamente os dados usando todas as rotas disponíveis. A API se conecta e utiliza os dados vindos de outra API não desenvolvida pelo grupo. |
|    B     | Atingiu o conceito C+ e o servidor está hospedado e acessível na AWS. Há um link para a API no arquivo README do projeto. |
|    B+    | Atingiu o conceito B e há testes de unidade para as rotas da API. |
|    A     | Atingiu o conceito B+ e há um sistema de autenticação implementado tanto no React quanto no Flask. |
|    A+     | Atingiu o conceito A e a foi feito deploy do cliente React na AWS. |