# JavaScript Assíncrono e Requisições HTTP

### Introdução
Até agora, tanto no Django quanto no Flask, toda vez que clicamos em um botão, a página inteira é recarregada. Isso é chamado de **comportamento síncrono**, onde uma ação só é executada após a conclusão da anterior. No entanto, em muitos casos, queremos que a página seja atualizada sem recarregar. Isso acontece quando damos um like em uma postagem do Facebook, por exemplo. 

A tecnologia que permite isso é o **JavaScript assíncrono**. Com ele, podemos fazer requisições a servidores sem recarregar a página, atualizar elementos da página dinamicamente, e muito mais.

Para podermos fazer requisições a servidores, usamos o **Axios**, uma biblioteca que facilita o uso de requisições HTTP. Neste handout, vamos aprender sobre Promises, async/await, Axios e como usá-los para fazer requisições HTTP. Isso será útil para a APS2, onde vocês vão precisar fazer requisições a um servidor para resolver exercícios e para entender o React, que é uma biblioteca JavaScript muito usada para criar interfaces de usuário.

## Axios: Biblioteca para Requisições
O **Axios** é uma biblioteca para realizar requisições HTTP com suporte a **Promises** e **async/await**.

Para poder executar código JavaScript pelo terminal é necessário instalar o Node.js. Baixe e instale o Noje.js [neste link](https://nodejs.org/pt-br/download/package-manager/).

### Instalando o Axios:
```sh
npm install axios
```

### Criando uma Instância do Axios
Podemos criar uma instância do Axios para configurar opções padrões.
```javascript
const axios = require("axios");
const instance = axios.create({
  baseURL: "https://api.exemplo.com",
  headers: { "Content-Type": "application/json" }
});
```

### Fazendo uma Requisição GET
```javascript
async function getData() {
    try {
        let response = await instance.get("/dados");
        console.log(response.data);
    } catch (error) {
        console.error("Erro na requisição:", error);
    }
}
getData();
```

### Fazendo uma Requisição POST
```javascript
async function postData() {
    try {
        let response = await instance.post("/enviar", { nome: "Marcio" });
        console.log("Dados enviados com sucesso:", response.status);
    } catch (error) {
        console.error("Erro ao enviar dados:", error);
    }
}
postData();
```


## Promises

Quando executamos uma linha como a seguir:

```javascript
let response = instance.get("/dados");
```

A função `instance.get` retorna uma *Promise*, que é um objeto que representa o resultado de uma operação assíncrona.

Uma *Promise* representa um valor que pode estar disponível agora, no futuro ou nunca.

### Estados de uma Promise:
- **Pending** (*Pendente*): A operação ainda não foi concluída.
- **Fulfilled** (*Realizada*): A operação foi bem-sucedida.
- **Rejected** (*Rejeitada*): A operação falhou.

Diferentemente do python, onde esperamos que a operação seja concluída para continuar o código, quando usamos JavaScript assíncrono isso não é verdade.

Se executarmos o seguinte código:

```javascript
let response = instance.get("/dados");
console.log(response.data);
```

Podemos ter comportamentos diferentes dependendo do tempo que a requisição demora para ser concluída. Se a requisição for respondida imediatamente, o código acima imprime os dados que voltaram do servidor. No entanto, se a requisição demorar, o código acima imprime `undefined`. Isso acontece porque o que é armazenado na veriável `response` é uma *Promise*, e não o valor retornado pelo servidor. Como lidamos com esse problema então?

Uma possibilidade é utilizar o comando `await`. O comando `await` pausa a execução da função até que a *Promise* seja resolvida. Veja o exemplo abaixo:

```javascript
let response = await instance.get("/dados");
console.log(response.data);
```

Dessa forma, o código acima imprime os dados que voltaram do servidor, independentemente do tempo que a requisição demorar para ser concluída.

O problema é que não temos nenhuma garantia de quanto tempo a requisição vai demorar para ser concluída. Se a requisição demorar muito, o código acima vai travar a execução do programa. É como se o Facebook travasse até que o like fosse computado no servidor. Essa não é uma boa experiência para o usuário.

Para resolver esse problema, podemos usar o comando `then`. O comando `then` é executado quando a *Promise* é resolvida. Veja o exemplo abaixo:

```javascript
instance.get("/dados").then(response => {
    console.log(response.data);
});
```

Esse código apresenta uma novidade para quem não está acostumado com JavaScript. O comando `then` é uma função que recebe outra função como argumento. Essa função é chamada de *callback*. O *callback* é executado quando a *Promise* é resolvida. Olhando por partes, o código que passamos dento do `then` é o seguinte:

```javascript
response => {
    console.log(response.data);
}
```

Esse código é uma função **anônima** (veja que não definimos nome nenhum) que recebe um argumento `response` e executa o código que está entre as chaves `{}`. O código acima é equivalente ao seguinte:

```javascript
function callback(response) {
    console.log(response.data);
}
instance.get("/dados").then(callback);
```

Como a função `callback` é simples e só é usada uma vez, é comum passar a função diretamente como argumento do `then`. Essa é uma maneira muito mais limpa de escrever o código. O método `then` é responsável por receber o valor retornado pela *Promise* e executar a função de *callback* passando o valor retornado como parâmetro para a função de *callback*.

## Async/Await
A palavra-chave **async** permite definir funções assíncronas, enquanto **await** pausa a execução da função até que uma *Promise* seja resolvida.

Exemplo:
```javascript
async function fetchData() {
    try {
        let response = await fetch("https://api.exemplo.com/dados");
        let data = await response.json();
        console.log(data);
    } catch (error) {
        console.error("Erro na requisição:", error);
    }
}
fetchData();
```

É importante lembrar que a palavra-chave **await** só pode ser usada dentro de funções assíncronas. Se tentarmos usar **await** fora de uma função assíncrona, um erro acontecerá.

## Erros Comuns
### 1. Não usar `await` em chamadas assíncronas
Errado:
```javascript
function getData() {
    let response = instance.get("/dados");
    console.log(response.data);
}
getData();
```
Correto:
```javascript
async function getData() {
    let response = await instance.get("/dados");
    console.log(response.data);
}
getData();
```

### 2. Esquecer de tratar erros com `try/catch`
Errado:
```javascript
async function getData() {
    let response = await instance.get("/dados");
    console.log(response.data);
}
```
Correto:
```javascript
async function getData() {
    try {
        let response = await instance.get("/dados");
        console.log(response.data);
    } catch (error) {
        console.error("Erro na requisição:", error);
    }
}
```


## Conclusão
- **Axios** é uma ferramenta eficiente para realizar requisições HTTP.
- **Promises** permitem executar código assíncrono de forma encadeada.
- **async/await** simplifica a escrita de código assíncrono.
- **Boas práticas** incluem sempre tratar erros e garantir que await seja usado corretamente.

Agora você já pode resolver a APS2!

