# 01 - Get-it - O retorno

## Parte 2: Respondendo com páginas HTML

Nosso servidor já responde com `Hello World`, mas queremos muito mais que isso. Queremos implementar o nosso Get-it e para isso a página precisa ter muito mais conteúdo e precisa ser apresentado de maneira estruturada. Está na hora de trazermos o bom e velho HTML de volta!

Vamos devolver uma página HTML simples, apenas para relembrar as coisas:

```python hl_lines="5-18 26"
--8<-- "01-getit/codigo/passo5.py"
```

Testou? Funcionou? Podemos ir para o próximo passo.

## Mostrando a lista de anotações

Podemos começar a pensar no conteúdo da nossa página principal. Vamos começar mostrando uma lista simples com os títulos e detalhes das anotações. Você vai precisar baixar a seguinte [imagem clicando neste link](codigo/img/logo-getit.png). Através do terminal, crie uma pasta chamada `static`. Dentro desta pasta, crie outra pasta chamada `img`. Salve essa imagem dentro da pasta `img`. Ou seja, o conteúdo do seu repositório será:

```
- DIRETORIO-DO-SEU-SERVIDOR
  |- servidor.py
  |- static
    |- img
      |- logo-getit.png
```

Para a lista de anotações vamos utilizar as tags HTML *unordered list* (`#!html <ul>`), *list item* (`#!html <li>`), *heading* (`#!html <h3>`) e *paragraph* (`#!html <p>`). Além disso, vamos mostrar uma imagem com o logo ao invés de um texto com o título:

```python hl_lines="13 16-45"
--8<-- "01-getit/codigo/passo6.py"
```

Se você rodou o código acima deve ter percebido que algo deu errado. Você não achou que seria tão simples assim, não é mesmo?

O arquivo da imagem do logo existe no seu computador (ou deveria existir - caso contrário, não se esqueça de baixar as imagens), mas o servidor precisa enviar esses arquivos como resposta quando forem solicitados.

## Diferenciando rotas

Temos que implementar algumas coisas, mas vamos por partes. Verifique a saída no seu terminal. Você deve encontrar algo assim:

```
127.0.0.1 - - [24/Jan/2025 14:27:28] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [24/Jan/2025 14:27:28] "GET /img/logo-getit.png HTTP/1.1" 404 -
127.0.0.1 - - [24/Jan/2025 14:27:28] "GET /favicon.ico HTTP/1.1" 404 -
```

Quando o navegador acessa a página, ele faz uma requisição para `/`. Esta requisção é respondida com a página HTML que criamos. Dentro desse HTML, temos um link para a imagem do logo. O navegador então faz uma nova requisição para `/img/logo-getit.png`. Como somente definimos uma resposta para `/`, o servidor responde com um erro 404, que é  o código HTTP para "não encontrado".

Altere novamente o código do seu servidor para:

```python hl_lines="1 13 51-52 56-59"
--8<-- "01-getit/codigo/passo7.py"
```

O comando `{{ url_for('static', filename='img/logo-getit.png') }}` é uma função do Flask que gera a URL para um arquivo estático. O Flask sabe que os arquivos estáticos estão no diretório `static` e que o arquivo `logo-getit.png` está dentro do diretório `img`. O Flask vai gerar a URL correta para o arquivo, independente de onde o servidor estiver rodando.
Agora, quando o servidor receber uma requisição para `/img/logo-getit.png`, ele vai procurar o arquivo no diretório `static/img` e enviar o conteúdo do arquivo como resposta. Se o arquivo não for encontrado, o servidor vai responder com um erro 404.

Depois de atualizar o código, o servidor deve funcionar corretamente, mostrando a imagem. Sim, está feio, mas nós resolvemos isso no próximo handout. Por enquanto vai ficar assim mesmo.

As páginas de detalhes ainda não estão prontas, mas antes disso precisamos refatorar o código porque ele já está acumulando muitas responsabilidades. Depois de se hidratar e fazer um alongamento, siga para a [parte 3 do handout](parte3.md).
