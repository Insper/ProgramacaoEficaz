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

Vamos implementar um servidor **bastante** simplificado utilizando a biblioteca Flask. Para isso, crie dentro da pasta `getit` criada anteriormente um arquivo chamado `servidor.py` (pode ser o nome que você preferir) com o seguinte conteúdo:
   
```python
--8<-- "01-getit/codigo/passo1.py"
```
    
Antes de tentarmos entender o código, execute-o para vermos o que ele faz. Para isso, abra um terminal, ative o ambiente virtual e execute o arquivo `servidor.py`:

```bash
python servidor.py
```

Você deve ver uma mensagem parecida com esta:

```bash
ModuleNotFoundError: No module named 'flask'
```

O erro ocorreu porque o Flask não está instalado no seu ambiente virtual. Para corrigir isso, instale o Flask utilizando o `pip`:

```bash
pip install flask
```

Agora sim, execute o servidor novamente. Se tudo ocorrer bem, você verá uma mensagem parecida com esta:

```
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 100-429-768
```

Essa mensagem indica que o servidor está rodando e pronto para receber requisições.

Abra o navegador de sua preferência e entre no endereço apresentado pelo seu programa. No exemplo acima, o endereço é `http://127.0.0.1:5000`

!!! danger "Atenção"
    Alguns navegadores podem não funcionar como esperado. Desta forma, teste em outros navegadores.

Você deve estar vendo uma página em branco. Se não estiver, tente acessar o endereço a partir de outro navegador. Se mesmo assim não funcionar, verifique se o servidor está rodando e se o endereço está correto.

## Muito bem, agora vamos entender o código acima

Flask é um microframework web escrito em Python, projetado para ser leve, flexível e fácil de usar. Ele é amplamente utilizado para desenvolver aplicações web, permitindo que os desenvolvedores construam projetos de forma rápida e eficiente. É possível ver nele algumas características que vimos no Django, mas de forma mais simplificada.

- `app = Flask(__name__)` cria uma instância da classe Flask, que será a base da aplicação. O argumento `__name__` é uma variável pré-definida em Python que contém o nome do módulo atual. Flask usa o nome do módulo para determinar a localização dos arquivos estáticos (como imagens e arquivos html).

- `@app.route('/')`: Define a rota principal da aplicação, ou seja, o que acontece quando você acessa `http://127.0.0.1:5000/` no navegador. A função logo abaixo é chamada toda vez que alguém acessa essa rota.
- `print(request.method)`: Exibe no terminal o método HTTP usado na requisição, como GET, POST, etc.
- `print(request.headers)`: Exibe no terminal todos os cabeçalhos da requisição HTTP, que incluem informações como o tipo de navegador, o tipo de conteúdo aceito e outras configurações do cliente.
- `return ""`: Retorna uma resposta vazia para o cliente, ou seja, não renderiza nada no navegador.

O restante do código inicia o servidor Flask e habilita o modo de depuração (debug mode), que recarrega automaticamente o servidor ao modificar o código e exibe mensagens detalhadas de erro no navegador, úteis para desenvolvimento.

## Entendi, mas então como eu faço algo aparecer no navegador?

Calma, pequeno gafanhoto. Antes de prosseguir, vamos entender mais alguns detalhes do que aconteceu até o momento.

Quando acessamos o endereço `http://127.0.0.1:5000/` no navegador, o navegador enviou uma requisição para o servidor. O servidor recebeu essa requisição e identificou qual a rota requisitada. No nosso caso, a rota requisitada foi a raiz do servidor, ou seja, a rota `/`. O servidor então executou a função associada a essa rota e retornou uma resposta vazia.

Dentro da função associada à rota `/`, existem dois prints. O primeiro printa o método HTTP utilizado na requisição, que no nosso caso é o método GET. O segundo printa os cabeçalhos da requisição, que contém informações como o tipo de navegador, o tipo de conteúdo aceito e outras configurações do cliente. Toda vez que um navegador quer se comunicar com um servidor, ele envia uma requisição HTTP contendo essas informações.

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

    Escolha o opção verdadeira:

    - [ ] O texto representa um Servidor de Nome de Domínio.
    - [ ] O texto representa uma resposta HTTP.
    - [X] O texto representa uma requisição HTTP.
    - [ ] O texto representa os dados enviados pelo Cliente.

    !!! details "Resposta"
        O texto representa uma requisição HTTP. Para mais detalhes veja [(request)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview#requests). 

## E agora, já podemos enviar a resposta?

Sim! Agora estamos prontos. Sem mais delongas, altere a seguinte linha no seu código:

```python hl_lines="10"
--8<-- "01-getit/codigo/passo3.py"
```

Acesse novamente a página pelo seu navegador. Pronto, nosso primeiro servidor está funcionando e retornando uma resposta!

!!! danger "Importante"
    Servidores são como programas em loop infinito. Se quiser parar de rodar, basta encerrar o programa com ++ctrl+c++.

Agora é só seguir para a [parte 2 deste handout](parte2.md).
