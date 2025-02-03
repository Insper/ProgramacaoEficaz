# APS 1

!!! success "Entrega"
    :date: 22/02 (sábado)
    
    :clock1: até as 23:59

    :material-account-group: Individual

    :simple-github: Entrega via :point_right: Blackboard.
 
## Para que preciso aprender isso?

Como comentado na aula, o banco de dados é uma parte muito importante nas diferentes arquiteturas de software, necessitando cuidados especiais na sua criação e manipulação. Vamos nesta APS praticar comandos da linguagem SQL com o objetivo de:
- Reconhecer a linguagem SQL para o envio de instruções para um banco de dados.
- Identificar os comandos de criação de tabelas e manipulação de dados, incuindo os principais parâmetros.

## Não sei nada sobre SQL! Por onde começo?

Uma das competências importantes para o cientista da computação é exercitar o aprender a aprender e portanto vocês podem buscar os conhecimentos que precisam em boas fontes de dados. Hoje existe algumas fontes na Internet que pode ajudar muito, tais como:

- W3 Schools (https://www.w3schools.com/): uma plataforma mantida na Noruega com tutoriais de aprendizado e experimentação para várias linguagens, inclusive o SQL. Você pode encontrar tudo o que precisa lá!
- SQLite Tutorial (https://www.sqlitetutorial.net/): como iremos trabalhar nesta APS com o SQLite, este tutorial pode também te auxiliar no desenvolvimento dos exercícios.

*Lembrando que as respostas dos exercícios serão liberados após a entrega da APS e iremos comentar em sala de aula cada resolução.*

## O que você precisa saber e fazer antes de iniciar os exercícios

- Você não precisa (neste momento) utilizar o SQLite instalado em seu computador para trabalhar com esta APS mas não impedimos caso queira desenvolver os exercícios em uma instância local.
- Sugerimos o uso de um sandbox executado 100% no navegador, acessando pela URL https://www.convertcsv.com/sqlite-online.htm
- Faça o download da base de dados [imoveis.db](imoveis.db)
- Faça a carga do banco de dados clicando no botão `Load an SQLite database` e selecionando o arquivo acima. Depois de executado com sucesso, a tabela `imoveis` estará carregada no banco de dados e você pode iniciar a resolução dos exercícios.
- A entrega dos exercícios deve ser enviada em PDF pelo Blackboard com texto gerado em LaTeX, usando o template disponível em https://www.overleaf.com/read/zgybjvrygnfw#19e451

## Como será a avaliação?

O feedback referente a esta atividade será disponibilizado a todos os alunos, indicando as questões corretas e incorretas incluindo as sugestões para melhoria. O conceito na atividade será atribuído pelo número de questões corretas, como segue a Tabela abaixo:

| Conceito | Número de Acertos |
| :------: | :-------- |
|    I     | 0 |
|    D     | 2 |
|    C     | 4 |
|    C+    | 6 |
|    B     | 8 |
|    B+    | 10 |
|    A     | 12 |
|    A+    | 14 |

**Reforçamos que não serão aceitos exercícios entregues fora do prazo e que na entrega não realizada será atribuído conceito I**

## Exercícios :material-check:

1. Selecione todos os campos de todos os imóveis.
2. Selecione o logradouro, bairro e cidade de todos os apartamentos.
3. Selecione o campo valor dos imóveis, renomeando o mesmo para "Preço", e mostre apenas os imóveis do tipo `casa em condominio`.
4. Conte quantos terrenos estão registrados na tabela.
5. Selecione todos os campos dos imóveis na cidade `Danielmouth`, ordenados pelo valor de forma decrescente.
6. Selecione os bairros e valores dos imóveis cujo valor esteja entre 300.000 e 500.000.
7. Conte quantos imóveis existem em cada bairro e exiba os resultados em ordem crescente de quantidade.
8. Selecione o maior e o menor valor de imóveis do tipo `casa`.
9. Selecione todos os campos dos imóveis cujo logradouro contenha a palavra `Court`.
10. Selecione os logradouros e tipos dos imóveis, ordenando primeiro por tipo de forma ascendente e depois por logradouro de forma descendente.
11. Suponha que todos os imóveis do tipo `apartamento` tiveram uma valorização de 10% devido a melhorias na infraestrutura local. Atualize o valor desses imóveis, aumentando-os em 10%.
12. Foi identificado um erro nos registros de todos os imóveis localizados no bairro `South Nicholas`, onde os CEPs foram cadastrados incorretamente. Atualize o CEP de todos os imóveis do bairro `South Nicholas` para o valor `123987`.
13. Suponha que a imobiliária decidiu remover do seu catálogo todos os imóveis adquiridos antes de $1^o$ de janeiro de 2010, pois eles consideram esses imóveis muito antigos para as necessidades atuais do mercado. Escreva um comando SQL que exclua todos os imóveis da tabela `imoveis` que foram adquiridos antes dessa data.
14. A imobiliária percebeu que os terrenos na cidade de `East Nicholas` não estão tendo a saída esperada e decidiu removê-los de sua lista de ofertas. Crie um comando SQL para excluir todos os registros de terrenos localizados em `East Nicholas`.