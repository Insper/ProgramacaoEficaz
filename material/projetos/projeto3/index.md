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

## Avaliação do Grupo :octicons-people-16:

A Rubrica do projeto será utilizada para avaliar o projeto submetido. No entanto, os membros do grupo podem ter sua nota alterada de acordo com o desempenho individual. Alunos que não tiverem quantidades significativas de commits com contribuições em seu nome, ou que não participarem ativamente do projeto, podem ter sua nota reduzida.

Para isso, será utilizada a avaliação por pares. Uma vez por semana, os membros do grupo devem preencher o formulário de avaliação por pares. Neste formulário, cada membro do grupo deve avaliar os outros membros do grupo. Serão 3 submissões do formulário, nos dias 23/04, 30/04 e 07/05. A não entrega de um dos formulários resultará em uma redução de meio conceito na nota final do aluno para cada formulário não entregue. 

No formulário, devem ser avaliadas a produtividade e proatividade de cada membro do grupo em uma escala de 1 a 5 da seguinte forma:

### Produtividade

1. Produziu muito abaixo do esperado, colocando a entrega em risco e obrigando outro(s) membro(s) a mudar planejamentos pessoais para garanti-la.

2. Produziu abaixo do esperado.

3. Produziu precisamente o esperado. Nem menos, nem mais.

4. Produziu acima do esperado.

5. Produziu muito acima do esperado, mudando planejamentos pessoais para compensar a entrega abaixo do esperado de outro(s) membro(s).

!!! danger "ATENÇÃO"
    - Se a sprint não foi bem sucedida, é obrigatório que pelo menos um dos membros tenha nível 1 ou 2. Não faz sentido todos terem produzido o esperado e ainda assim a sprint ter sido malsucedida.

    - Se um membro tem nível 5, é obrigatório, pela descrição da rubrica, que pelo menos um dos membros tenha nível 1 ou pelo menos dois dos membros tenham nível 2.

    - Para atingir A, tanto faz atribuir 3 ou 4. Ou seja, não faz muito sentido atribuir 4 por receio de prejudicar o colega. Use esse nível para reconhecer desempenhos excepcionais.

### Proatividade

1. Nem tentou fazer o que tinha prometido.

2. Tentou fazer o que tinha prometido, mas só porque o grupo ficou cobrando.

3. Tentou fazer o que tinha prometido, sem que o grupo precisasse ficar cobrando.

4. Terminou o que tinha prometido e tentou fazer além, ajudando outro(s) membro(s) que estava(m) tendo dificuldades.

5. Tentou fazer o que outro(s) membro(s) tinha(m) prometido, mesmo sem terminar o que ele próprio tinha prometido e/ou sem ter evidência de que esse(s) esse(s) membro(s) estava(m) tendo dificuldades.

| Conceito | Descrição |
| :------: | :-------- |
|    Sem desconto    | Não teve nenhuma avaliação abaixo do esperado. Ou teve uma avaliação abaixo do esperado, seguida de duas avaliações acima do esperado. |
|    Menos meio conceito     | Teve avaliação abaixo do esperado em 1 sprint. |
|    Menos um conceito     | Teve avaliação abaixo do esperado em 2 sprints. |
|    Menos dois conceitos     | Teve avaliação de desempenho abaixo do esperado em 3 sprints. |
|    Menos três conceitos     | Não respondeu nenhum questionário dentro do prazo. Ou não possui nenhum contribuição significativa no projeto.|

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