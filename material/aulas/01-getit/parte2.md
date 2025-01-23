# 01 - Get-it - O retorno

## Parte 2: Respondendo com páginas HTML

Nosso servidor já responde com `Hello World`, mas queremos muito mais que isso. Queremos implementar o nosso Get-it e para isso a página precisa ter muito mais conteúdo e precisa ser apresentado de maneira estruturada. Está na hora de trazermos o bom e velho HTML de volta!

Mas antes disso, nosso servidor atualmente responde uma requisição e para de rodar. Seria interessante que ele fosse capaz de responder mais do que uma requisição. Modifique seu programa da seguinte maneira:

```python hl_lines="13"
--8<-- "01-getit/codigo/passo4.py"
```

A única diferença é que colocamos a parte do código que aceita a conexão do cliente, recebe a requisição e devolve a resposta dentro de um `#!python while True`. Então podemos recarregar a página no navegador quantas vezes quisermos e ela continuará a ser recebida.

!!! danger "Importante"
    Agora o servidor é um programa em loop infinito. Se quiser parar de rodar, basta encerrar o programa com ++ctrl+c++.

## Agora sim, o HTML

Vamos devolver uma página HTML simples, apenas para relembrar as coisas:

```python hl_lines="6-21 37"
--8<-- "01-getit/codigo/passo5.py"
```

Testou? Funcionou? Podemos ir para o próximo passo.

## Mostrando a lista de anotações

Podemos começar a pensar no conteúdo da nossa página principal. Vamos começar mostrando uma lista simples com os títulos e detalhes das anotações. Você vai precisar baixar a seguinte [imagem clicando neste link](codigo/img/logo-getit.png). Salve essa imagem dentro de uma pasta `img` na mesma pasta onde está o seu código do servidor. Ou seja, o conteúdo da sua pasta será:

```
- DIRETORIO-DO-SEU-SERVIDOR
  |- servidor.py
  |- img
     |- logo-getit.png
```

Para a lista de anotações vamos utilizar as tags HTML *unordered list* (`#!html <ul>`), *list item* (`#!html <li>`), *heading* (`#!html <h3>`) e *paragraph* (`#!html <p>`). Além disso, vamos mostrar uma imagem com o logo ao invés de um texto com o título:

```python hl_lines="16 19-48"
--8<-- "01-getit/codigo/passo6.py"
```

Se você rodou o código acima deve ter percebido que algo deu errado. Você não achou que seria tão simples assim, não é mesmo?

O arquivo da imagem do logo existe no seu computador (ou deveria existir - caso contrário, não se esqueça de baixar as imagens), mas o servidor precisa enviar esses arquivos como resposta quando forem solicitados.

## Diferenciando rotas

Temos que implementar algumas coisas, mas vamos por partes. Verifique a saída no seu terminal. Você deve encontrar vários blocos de texto, um para cada requisição feita pelo navegador. Alguns exemplos:

=== "favicon.ico"

    ```
    GET /favicon.ico HTTP/1.1
    Host: 0.0.0.0:8080
    Connection: keep-alive
    Pragma: no-cache
    Cache-Control: no-cache
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
    Accept: image/avif,image/webp,image/apng,image/*,*/*;q=0.8
    Referer: http://0.0.0.0:8080/
    Accept-Encoding: gzip, deflate
    Accept-Language: en-US,en;q=0.9,pt;q=0.8
    ```

=== "logo-getit.png"

    ```
    GET /img/logo-getit.png HTTP/1.1
    Host: 0.0.0.0:8080
    Connection: keep-alive
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36
    Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8
    Referer: http://0.0.0.0:8080/
    Accept-Encoding: gzip, deflate
    Accept-Language: en-US,en;q=0.9,pt;q=0.8
    ```


O nosso servidor responde a mesma página HTML para **todas as requisições**. Não importa se o cliente está pedindo a imagem `/img/logo-getit.png` ou o `favicon.ico`. Ele **sempre** responde com a mesma página HTML.

Repare que a primeira linha da requisição HTTP sempre possui uma palavra (`GET` - voltaremos a falar sobre ele mais para a frente no curso) seguida de uma rota (por exemplo, `/img/logo-getit.png`). Nós podemos utilizar essa rota no servidor para decidir o que devemos responder.

Altere novamente o código do seu servidor para:

```python hl_lines="2-3 5 27-33"
--8<-- "01-getit/codigo/passo7.py"
```


Crie também o arquivo `utils.py` na pasta do seu servidor. Você deverá implementar os métodos `#!python extract_route` e `#!python read_file`. Para te ajudar, baixe também o arquivo [`test_utils.py`](codigo/test_utils.py). Ele possui alguns testes para verificar se a sua implementação está dentro do esperado. 

Para executar os testes basta rodar o arquivo no terminal (ele tem alguns testes para outras funções das próximas partes do handout - você pode ignorar os erros delas por enquanto).: 

    python test_utils.py

Ao rodar os teste a saída do terminal deverá ser algo parecido com as mensagens a seguir:

    A função extract_route não foi implementada, portanto não é possível testá-la.
    A função read_file não foi implementada, portanto não é possível testá-la.
    A função load_data não foi implementada, portanto não é possível testá-la.
    A função load_template não foi implementada, portanto não é possível testá-la.
    A função build_response não foi implementada, portanto não é possível testá-la.

    ----------------------------------------------------------------------
    Ran 0 tests in 0.000s

    OK

!!! example "EXERCÍCIO"
    Implemente a função `#!python extract_route`, que recebe uma string com a requisição e devolve a rota, excluindo o primeiro caractere (`#!python /`).

    Por exemplo, para a requisição:
    ```
    GET /img/logo-getit.png HTTP/1.1
    Host: 0.0.0.0:8080
    Connection: keep-alive
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36
    Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8
    Referer: http://0.0.0.0:8080/
    Accept-Encoding: gzip, deflate
    Accept-Language: en-US,en;q=0.9,pt;q=0.8
    ```

    Sua função deve devolver `#!python 'img/logo-getit.png'`. 

!!! tip "Dica"
    É possível verificar se a implementação da função pedida no exercício anterior está correta, basta rodar os testes.
    Por exemplo, se a implementação da função `extract_route` não estiver correta, então algumas mensagens de erro serão apresentadas no terminal ao rodar os testes.

!!! question choice
    No código do `servidor.py`, adicionamos um import para a biblioteca `#!python pathlib`. Essa biblioteca é utilizada para manipulação de caminhos de arquivos e diretórios. Qual o conteúdo da variável `CUR_DIR` após a execução do código a seguir?


    ```python
    CUR_DIR = Path(__file__).parent
    ``` 
       
    Escolhe a opção correta:

    - [X] `CUR_DIR` é uma string com o caminho do diretório onde o arquivo `servidor.py` está localizado.
    - [ ] `CUR_DIR` é uma string com o caminho do diretório onde o arquivo `servidor.py` está localizado, mas com o nome do arquivo incluso.
    - [ ] `CUR_DIR` é uma string com o caminho do diretório onde o arquivo `servidor.py` está localizado, mas com o nome do arquivo e a extensão inclusos.
    - [ ] `CUR_DIR` é uma string com o caminho do diretório onde o arquivo `servidor.py` está localizado, mas com o nome do arquivo, a extensão e o nome do diretório inclusos.

    !!! details "Resposta"
        A variável `CUR_DIR` é uma string com o caminho do diretório onde o arquivo `servidor.py` está localizado. Ou seja, será algo como `'/home/usuario/tecweb/aulas/01-getit'`.
        Para mais detalhes acesse: https://docs.python.org/3/library/pathlib.html#pathlib.Path.parent

!!! question choice
    Ainda explorando o uso da biblioteca `#!python pathlib`, o que será impresso no terminal ao executar o código a seguir?

    Suponha que a variável `CUR_DIR` seja a string `/home/usuario/tecweb/aulas/01-getit`

    ```python
    CUR_DIR = Path(__file__).parent
    route = 'img/logo-getit.png'
    filepath = CUR_DIR / route
    print(filepath)
    ``` 
       
    Escolhe a opção correta:

    - [ ] `img/logo-getit.png`
    - [ ] `/home/usuario/tecweb/aulas/01-getit`
    - [X] `/home/usuario/tecweb/aulas/01-getit/img/logo-getit.png`
    - [ ] Ocorrerá algum erro.

    !!! details "Resposta"
        Será impresso `/home/usuario/tecweb/aulas/01-getit/img/logo-getit.png`, pois a operação `/` entre dois objetos do tipo `#!python Path` concatena os caminhos. Para mais detalhes acesse: https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.__truediv__

        Ao desenvolver aplicações que manipulam arquivos e diretórios, é comum utilizar a biblioteca `#!python pathlib` para manipular caminhos de arquivos e diretórios. Não é uma boa prática utilizar caminhos absolutos.

!!! example "EXERCÍCIO"
    Implemente a função `#!python read_file`, que recebe um argumento do tipo [`#!python Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path) e devolve o conteúdo desse arquivo. Sua função deve ler o arquivo e devolver o conteúdo como binário (`#!python bytes`). Se precisar refrescar a memória, leia a [documentação da função `#!python open`](https://docs.python.org/3/library/functions.html#open).

Depois de implementar as duas funções acima e atualizar o código, o servidor deve funcionar corretamente, mostrando as imagens. Sim, está feio, mas nós resolvemos isso na próxima aula. Por enquanto vai ficar assim mesmo.

As páginas de detalhes ainda não estão prontas, mas antes disso precisamos refatorar o código porque ele já está acumulando muitas responsabilidades. Depois de se hidratar e fazer um alongamento, siga para a [parte 3 do handout](parte3.md).
