# 01 - Get-it - O retorno
    
## Parte 1: Criando o servidor

Vamos começar nosso curso com um exemplo de implementação de uma página bem simples. Durante o desenvolvimento discutiremos alguns dos detalhes e conceitos envolvidos. O objetivo deste handout é introduzir alguns conceitos de Programação Eficaz que serão importantes ao longo do curso a partir de uma abordagem mão na massa.

Após o final deste handout você terá um protótipo do Get-it, nosso conhecido sistema de bloco de notas feito utilizando uma nova tecnologia.

## Começando pelo começo

Lembra que semestre passado nós aprendemos sobre os diferentes tipos de teste de software? Vamos começar definindo uma história de usuário. O objetivo não é fazer uma revisão de Design, então vamos assumir que temos uma persona pronta e o seu nome é Fábio:

!!!danger "Lista de anotações"
    **SENDO** o Fábio

    **POSSO** digitar o endereço do Get-it no navegador e visualizar a lista de anotações

    **PARA** lembrar os detalhes da minha próxima tarefa

Muito bem. Agora podemos começar a desenvolver o nosso protótipo.

Isso nos leva à primeira pergunta: ok, o Fábio vai digitar o endereço no navegador e apertar *Enter*, mas o que acontece depois disso?

MUITA coisa. Vamos começar com uma explicação bastante simplista, mas que deve dar uma ideia geral dos passos. Se você tiver curiosidade, a Mozilla possui um [material muito didático](https://developer.mozilla.org/pt-BR/docs/Aprender/Getting_started_with_the_web/Como_a_Web_funciona) para quem está iniciando no desenvolvimento web.

1. O navegador precisa dos dados da página a ser mostrada, mas a informação está em outro computador, o servidor, que está (muito provavelmente) fisicamente distante. Por isso, o endereço digitado no navegador é utilizado para encontrar a localização do servidor utilizando o [DNS](https://developer.mozilla.org/pt-BR/docs/Aprender/Getting_started_with_the_web/Como_a_Web_funciona#dns_explicado).
2. Agora que o cliente (o computador do Fábio) sabe onde encontrar o servidor, ele entra em contato com o servidor pedindo os dados. Esse pedido é o que chamamos de **requisição**.
3. Ao receber a requisição, o servidor responde com a página solicitada.
4. O navegador recebe as partes que formam a página (HTML, CSS, Javascript, imagens, etc.) e mostra (renderiza) para o Fábio.

Essa é uma lista bastante simplificada do que acontece, mas talvez esse último passo tenha sido simplificado demais. Cada parte que forma a página (os arquivos CSS, Javascript, imagens, etc.) deve ser solicitada separadamente para o servidor. Então os passos 1 a 3 são repetidos para cada uma delas.

## Você disse que seria mão na massa, mas ainda não toquei no código!

Eu sei, me desculpe. Agora sim, vamos começar!

Vamos implementar um servidor **bastante** simplificado em Python puro, sem nenhuma biblioteca. Para isso, crie uma nova pasta em seu computador e crie dentro dela um arquivo chamado `servidor.py` (pode ser o nome que você preferir) com o seguinte conteúdo (o exemplo deste handout foi baseado [neste código](https://www.codementor.io/@joaojonesventura/building-a-basic-http-server-from-scratch-in-python-1cedkg0842)):

!!!danger "Atenção"
    É possível que o endereço `0.0.0.0` não funcione no seu computador. Se isso acontecer, ao invés de acessar `0.0.0.0:8080`, acesse umas das opções a seguir:

    - `localhost:8080`
    - `127.0.0.0:8080`
    
```python
--8<-- "01-getit/codigo/passo1.py"
```
    
Antes de tentarmos entender o código, execute-o para vermos o que ele faz. O primeiro `#!python print` deve ter sido executado, mas o segundo não.

Abra o navegador de sua preferência e entre no endereço apresentado pelo seu programa. **Uma página de erro deve aparecer, mas não se desespere (se você me chamar porque não leu esta frase eu vou só apontar para ela e vou embora).**

!!! danger "Atenção"
    Alguns navegadores podem não funcionar como esperado. Desta forma, teste em outros navegadores.

Agora que você chegou nesta linha sem se desesperar, olhe para o terminal. O último `#!python print` foi executado (caso contrário, agora você pode me chamar)!

## Muito bem, agora vamos entender o código acima

O módulo `#!python socket` é utilizado para lidar com chamadas de rede em baixo nível. A [documentação oficial](https://docs.python.org/3/library/socket.html) pode ser útil para entender as funções utilizadas.

As constantes `#!python SERVER_HOST` e `#!python SERVER_PORT` definem o endereço do servidor (no caso, `0.0.0.0`) e a porta. Um computador pode ser acessado via rede através de uma porta. Por enquanto basta sabermos que um mesmo computador possui muitas portas e é necessário especificar qual porta queremos usar para a nossa conexão.

As outras linhas antes do primeiro `#!python print` basicamente dizem para o programa se conectar à porta desejada e aguardar requisições. O método `#!python accept()` trava a execução do programa até que uma requisição seja recebida.

Quando um cliente se conecta ao servidor (isso ainda não é a requisição), o programa realiza o segundo `#!python print`, fecha todas as conexões e termina. Note que o nosso servidor não enviou nenhuma resposta para o cliente e por isso o navegador mostrou a página de erro, dizendo que a página solicitada está inacessível.

## Entendi, mas então como eu envio a resposta?

Calma, pequeno gafanhoto. Antes de prosseguir, vamos entender mais alguns detalhes do que aconteceu até o momento.

Uma conexão foi criada, mas o servidor ainda não visualizou a requisição. Modifique o seu programa da seguinte maneira:

```python hl_lines="13-16"
--8<-- "01-getit/codigo/passo2.py"
```

Agora sim estamos lendo os dados enviados pelo cliente. No comando utilizado indicamos que queremos ler no máximo 1024 bytes. O resultado é devolvido como um valor do tipo `#!python bytes`, portanto convertemos ele para uma string utilizando o método `#!python decode()` (se tiver curiosidade, teste novamente sem o `#!python decode()` para ver o resultado).

O seu terminal deve ter mostrado uma saída parecida com esta (testei nos dispositivos que eu tinha disponíveis no momento):

=== "MacOS - Safari"

    ```
    GET / HTTP/1.1
    Host: 0.0.0.0:8080
    Upgrade-Insecure-Requests: 1
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15
    Accept-Language: en-us
    Accept-Encoding: gzip, deflate
    Connection: keep-alive
    ```

=== "MacOS - Firefox"

    ```
    GET / HTTP/1.1
    Host: localhost:8080
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:83.0) Gecko/20100101 Firefox/83.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
    Accept-Language: pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Connection: keep-alive
    Cookie: _ga=GA1.1.16347193.1542986176
    Upgrade-Insecure-Requests: 1
    ```

=== "Android - Chrome"

    ```
    GET / HTTP/1.1
    Host: 192.168.15.14:8080
    Connection: keep-alive
    Save-Data: on
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Linux; Android 11; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    Accept-Encoding: gzip, deflate
    Accept-Language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7
    ```

Sugiro que você também tente acessar o mesmo endereço a partir de navegadores e dispositivos diferentes. Caso você queira testar o acesso de um dispositivo diferente você vai precisar descobrir o IP do servidor.

Nos testes acima eu acessei o servidor a partir do Android e, no meu laptop, do Firefox e do Safari. É importante notar que cada um desses navegadores foi desenvolvido por empresas diferentes, no caso, Google, Mozilla e Apple. Mas então como todos eles conseguem se comunicar com o nosso servidor? É aí que entra o tal do HTTP.

Os 3 exemplos mostrados acima são muito semelhantes, apesar de virem de fabricantes diferentes. Isso acontece porque todos eles seguem o mesmo *protocolo*, o <b>H</b>yper <b>T</b>ext <b>T</b>ransfer <b>P</b>rotocol. O que precisamos saber por enquanto é que ele define como devem ser as requisições e respostas nessa comunicação. Como o HTTP é padronizado, se o seu servidor souber se comunicar em HTTP ele poderá se comunicar com qualquer navegador, independente das implementações específicas.

Nos exemplos nós podemos ver que o texto é enviado em um formato parecido com um dicionário: chaves, dois pontos e os valores. Esse conjunto de chaves e valores é o **cabeçalho (header)** da requisição [(request)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview#requests) ou resposta [(response)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview#responses). Como sempre, incentivo que você procure por conta própria mais detalhes sobre esse protocolo. Essa é apenas uma breve introdução.

!!! question choice
    Considere o texto a seguir:

        GET / HTTP/1.1
        Host: 192.168.15.14:8080
        Connection: keep-alive
        Save-Data: on
        Upgrade-Insecure-Requests: 1
        User-Agent: Mozilla/5.0 (Linux; Android 11; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
        Accept-Encoding: gzip, deflate
        Accept-Language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7

    Escolhe o opção verdadeira:

    - [ ] O texto representa um Servidor de Nome de Domínio.
    - [ ] O texto representa uma resposta HTTP.
    - [X] O texto representa uma requisição HTTP.
    - [ ] O texto representa os dados enviados pelo Cliente.

    !!! details "Resposta"
        O texto representa uma requisição HTTP. Para mais detalhes veja [(request)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview#requests). 

## E agora, já podemos enviar a resposta?

Sim! Agora estamos prontos. Sem mais delongas, adicione as seguintes linhas ao seu código:

```python hl_lines="18-19"
--8<-- "01-getit/codigo/passo3.py"
```

É essencial que existam duas quebras de linha (`#!python '\n'`) entre o `#!python 'HTTP/1.1 200 OK'` e o `#!python 'Hello World'`. Se houvesse apenas uma, o `#!python 'Hello World'` seria considerado como parte do cabeçalho da resposta.

Execute o servidor novamente e acesse a página pelo seu navegador. Pronto, nosso primeiro servidor está funcionando!

É só seguir para a [parte 2 deste handout](parte2.md).
