# 01 - Get-it - O retorno

## Parte 4: Fazendo um formulário de criação de anotação

Vamos implementar agora a funcionalidade de adicionar anotações. O objetivo é que você aprenda como receber dados no servidor enviados pelo navegador.

!!! danger "Atenção"
    É possível que nas próximas etapas o servidor apresente erros inesperados. Tente acessar o servidor de um navegador com aba anônima.

Para começar, modifique o template `index.html` para adicionar o `#!html <form>`:

```html hl_lines="6-12"
<!-- DOCTYPE, HTML, HEAD DEVEM CONTINUAR AQUI -->
<body>
  <img src="{{{{ url_for('static', filename='img/logo-getit.png') }}}}">
  <p>Como o Post-it, mas com outro verbo</p>

  <form action="/submit" method="POST">
    <label for="titulo">Título</label>
    <input id="titulo" type="text" name="titulo" />
    <label for="detalhes">Detalhes</label>
    <input id="detalhes" name="detalhes" />
    <input type="submit" />
  </form>
  <!-- O RESTO DO HTML A PARTIR DAQUI -->
```

Seu código do programa principal não precisa ser modificado ainda.

!!! example "EXERCÍCIO"
    Execute o servidor e teste a página.

    !!! danger "Importante"
        Quando você for testar a página, ao clicar em `submit` deve aparecer o erro `Not Found`. É isso mesmo que deve ocorrer. Nos próximos passos nós vamos resolver essa situação.

## Usando os dados recebidos do formulário

Talvez você tenha notado que no formulário (`<form>`) existe um atributo `method="post"`. Isso quer dizer que os dados do formulário serão enviados utilizando o método HTTP POST (veremos mais detalhes sobre ele no futuro). O que você precisa saber por enquanto é que até o momento nós sempre enviamos requisições do tipo GET para o servidor. Para entender melhor o que está acontecendo, observe a saída do seu terminal. Deve haver uma requisição parecida com essa:

```
127.0.0.1 - - [24/Jan/2025 15:35:41] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [24/Jan/2025 15:35:41] "GET /static/img/logo-getit.png HTTP/1.1" 200 -
127.0.0.1 - - [24/Jan/2025 15:35:41] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [24/Jan/2025 15:35:45] "POST /submit HTTP/1.1" 404 -
```

Perceba que a última linha da requisição está diferente das outras. Existe um `POST` ao invés de `GET`. Isso significa que o navegador está enviando dados para o servidor. O servidor, por sua vez, não sabe o que fazer com esses dados e responde com um erro `404`.

Queremos pegar os dados do formulário e extrair o título e os detalhes da anotação. No `form` do arquivo `index.html`, o campo `action` está apontando para `/submit`. Precisamos criar uma nova rota no servidor para lidar com essa requisição.

```python hl_lines="1 15-21"
--8<-- "01-getit/codigo/passo11.py"
```

Essa nova rota `/submit` foi definida para somente aceitar o método `POST`. Veja o que acontece se tentarmos acessar no navegador o endereço `http://localhost:5000/submit`. Leia a mensagem de erro e tente entender o que está acontecendo.

Chamar essa rota só vai fazer sentido se estivermos passando dados para ela. Por isso, deixamos ela responder somente a requisições do tipo `POST`. Utilizamos os comandos `request.form.get` para pegar os dados enviados pelo formulário. O método `get` é utilizado para pegar o valor de uma chave de um dicionário. Se a chave não existir, ele retorna `None`. `request.form`, assim como o `request.headers` que vimos anteriormente, é um dicionário que contém os dados enviados pelo navegador.

Assim como fazíamos no Django, toda requisição precisa ter uma resposta. Como não queremos ter nenhuma outra página após criar a nota, vamos retornar para a página inicial. Para isso, usamos o comando `return redirect('/')` assim como no Django.

!!! example "EXERCÍCIO"
    Crie uma função `#!python submit(titulo, detalhes)` no arquivo `views.py`, que adicione a nova anotação (que deverá estar armazenada em `#!python params['titulo']` e `#!python params['detalhes']`) ao arquivo `notes.json`.

    Dica: crie uma função no arquivo `utils.py` que recebe a nova anotação e a adiciona à lista do arquivo `notes.json`.

Teste seu servidor e verifique se as anotações estão sendo salvas corretamente. Se tudo estiver funcionando, a anotação deve estar aparecendo e no terminal você deve ver a seguinte mensagem:

```
127.0.0.1 - - [24/Jan/2025 16:12:42] "POST /submit HTTP/1.1" 302 -
127.0.0.1 - - [24/Jan/2025 16:12:42] "GET / HTTP/1.1" 200 -
```

Isso significa que o servidor recebeu a requisição do tipo `POST` e redirecionou para a página inicial. O número 302 é o código de status HTTP que indica que a requisição foi redirecionada. Isso também vai fazer com que atualizar a página não envie novamente os dados do formulário, assim como acontecia no Django.

## Desafio

O handout acabou, mas se quiser praticar um pouco mais você pode fazer o servidor devolver uma resposta com o código 404 quando a requisição é feita a uma página/recurso que não existe.

Além disso, você pode usar os arquivos HTML e CSS que construiu semestre passado para estilizar a página de anotações.

## Ufa, cansei

Parabéns! Agora você pode tentar fazer alguma das receitas da nossa lista de anotações. Depois disso, se ainda tiver pique, é um bom momento para dar aquela relembrada em CSS com essa lista de jogos:

- [Flexbox Defense](http://www.flexboxdefense.com/)
- [Flexbox Froggy](https://flexboxfroggy.com)
- [Grid Garden](https://cssgridgarden.com)
- [CSS Diner](http://flukeout.github.io/)
- Se você tem interesse por CSS, você vai gostar disso: https://rupl.github.io/unfold/
