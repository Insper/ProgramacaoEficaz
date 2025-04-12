# Autenticação com JWT

Quando trabalhamos com o servidor de exercícios JS, a primeira coisa que tivemos que fazer foi pedir para a API um token de autenticação. Nas requisições seguintes, tivemos que passar esse token para a API, para que ela pudesse nos identificar e liberar o acesso aos dados. Esse processo de autenticação é muito comum em aplicações web, e o JWT (JSON Web Token) é uma das formas mais populares de implementar isso.

## O que é JWT?

O JWT é um padrão que define uma maneira segura de gerar tokens que podem ser usados para autenticação. Essa geração utiliza princípios de criptografia, o que garante que o token não possa ser forjado. Assim, o cliente precisa enviar suas informações de autenticação (usuário e senha) apenas uma vez, e a partir daí, ele pode usar o token para acessar os dados protegidos.

## Backend

O backend é responsável por gerar o token e enviá-lo para o cliente. Para isso, ele precisa de um segredo (secret) que será usado para assinar o token. Esse segredo deve ser mantido em segurança, pois qualquer um que tenha acesso a ele pode gerar tokens válidos.
O backend também deve ter uma rota de login, onde o cliente envia suas credenciais (usuário e senha) e recebe o token em resposta. Esse token deve ser enviado em todas as requisições subsequentes para acessar os dados protegidos.

Para implementar o JWT na nossa API Flask, precisamos de algumas bibliotecas:
```
pip install flask flask-cors flask-jwt-extended flask-bcrypt
```
As bibliotecas flask e flask-cors já conhecemos. A biblioteca flask-jwt-extended é a responsável por implementar o JWT na nossa API, e a flask-bcrypt é usada para criptografar as senhas dos usuários, garantindo que elas não sejam armazenadas de maneira insegura no banco de dados. 

Veja um exemplo de implementação do JWT em uma API Flask:

```python
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from flask_bcrypt import Bcrypt
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
jwt = JWTManager(app)

client = MongoClient(os.getenv("MONGO_URI"))
db = client["login_db"]
usuarios_col = db["usuarios"]
notas_col = db["notas"]

@app.route("/cadastro", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if usuarios_col.find_one({"username": username}):
        return jsonify({"msg": "Usuário já existe"}), 400

    hashed = bcrypt.generate_password_hash(password).decode("utf-8")
    usuarios_col.insert_one({"username": username, "password": hashed})
    return jsonify({"msg": "Usuário cadastrado com sucesso"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = usuarios_col.find_one({"username": username})
    if not user or not bcrypt.check_password_hash(user["password"], password):
        return jsonify({"msg": "Usuário ou senha inválidos"}), 401

    token = create_access_token(identity=username)
    return jsonify(access_token=token)

@app.route("/notas", methods=["GET"])
@jwt_required()
def get_notas():
    username = get_jwt_identity()
    notas = list(notas_col.find({"username": username}, {}))
    return jsonify(notas)

if __name__ == "__main__":
    app.run(debug=True)
```

Nesse código temos vários comandos novos. Vamos ver o que cada um deles faz:
- `from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity`: Importa as funções e classes necessárias para trabalhar com JWT. Mais especificamente:
    - JWTManager: inicializa o JWT
    - create_access_token: gera um token para o usuário
    - jwt_required: protege rotas que exigem login
    - get_jwt_identity: recupera quem está autenticado

- `from flask_bcrypt import Bcrypt`: Importa a biblioteca Bcrypt, que é usada para criptografar senhas.

- `app.config["JWT_SECRET_KEY"] = "..."`: Define a chave secreta que será usada para assinar os tokens. Essa chave deve ser mantida em segredo e não deve ser exposta no código-fonte. Para isso, usamos a biblioteca dotenv, que carrega variáveis de ambiente de um arquivo `.env`. O arquivo `.env` deve conter a variável `JWT_SECRET_KEY` com o valor da chave secreta.

- `jwt = JWTManager(app)`: Inicializa o JWTManager com a aplicação Flask.

- `@jwt_required()`: Um decorator que protege a rota, exigindo que o usuário esteja autenticado para acessá-la. Se o usuário não estiver autenticado, ele receberá um erro 401 (não autorizado).

- `get_jwt_identity()`: Recupera a identidade do usuário autenticado. Essa identidade é o que foi passado como `identity` na hora de criar o token, que no nosso caso é o nome de usuário.

- `bcrypt.generate_password_hash(password).decode("utf-8")`: Criptografa a senha do usuário antes de armazená-la no banco de dados. O método `generate_password_hash` retorna um objeto bytes, então usamos o método `decode` para convertê-lo em uma string.

- `bcrypt.check_password_hash(user["password"], password)`: Verifica se a senha informada pelo usuário é igual à senha armazenada no banco de dados. Essa verificação é feita comparando o hash da senha informada com o hash armazenado no banco de dados. Não é possível reverter o hash para obter a senha original, então essa verificação é feita de forma segura.

- `create_access_token(identity=username)`: Cria um token de acesso para o usuário, usando o nome de usuário como identidade. Esse token será enviado para o cliente e deve ser incluído em todas as requisições subsequentes para acessar rotas protegidas.

## Frontend

No frontend, precisamos fazer algumas alterações para lidar com o token de autenticação. Quando o usuário fizer login, devemos armazenar o token em algum lugar e incluí-lo em todas as requisições subsequentes para acessar rotas protegidas. Os navegadores oferecem várias opções para armazenar dados, como cookies, localStorage e sessionStorage. A escolha de qual usar depende do caso de uso. Veja algumas considerações:
- **Cookies**: São enviados automaticamente pelo navegador em todas as requisições para o mesmo domínio. Isso pode ser útil para autenticação, mas também pode ser um problema de segurança se não forem configurados corretamente. É importante usar a flag `HttpOnly` para evitar que o JavaScript acesse o cookie, e a flag `Secure` para garantir que o cookie só seja enviado em conexões HTTPS.
- **localStorage**: É uma opção mais simples, mas os dados armazenados no localStorage podem ser acessados pelo JavaScript, o que pode ser um problema de segurança. Além disso, os dados no localStorage persistem mesmo após o fechamento do navegador, o que pode não ser desejável em alguns casos.
- **sessionStorage**: Funciona de maneira semelhante ao localStorage, mas os dados armazenados no sessionStorage são removidos quando o navegador é fechado. Isso pode ser útil para autenticação, pois os dados não persistem entre sessões.

No nosso caso, vamos usar o localStorage para armazenar o token de autenticação. Veja como ficaria a implementação do login no frontend:

No componente de login, vamos fazer uma requisição para a rota de login da API e armazenar o token no localStorage:
```javascript
import { useState } from "react";
import axios from "axios";

export default function Login({ onLogin }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("http://127.0.0.1:5000/login", {
        username,
        password,
      });
      const token = res.data.access_token;
      localStorage.setItem("token", token);
      onLogin(token);
    } catch (err) {
      alert("Login falhou");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input value={username} onChange={e => setUsername(e.target.value)} placeholder="Usuário" />
      <input value={password} type="password" onChange={e => setPassword(e.target.value)} placeholder="Senha" />
      <button type="submit">Entrar</button>
    </form>
  );
}
```

Nesse código, usamos o `localStorage` para armazenar o token de autenticação. Quando o usuário faz login, o token é salvo no localStorage e passado para a função `onLogin`, que pode ser usada para atualizar o estado do aplicativo e permitir que o usuário acesse as rotas protegidas. Essa função `onLogin` deve ser implementada no componente pai, que deve passar o token para os componentes que precisam dele. Veja um exemplo de como isso pode ser feito no arquivo `App.js`:

```javascript
// src/App.js
import { useState, useEffect } from "react";
import axios from "axios";
import Login from "./Login";

function App() {
  const [token, setToken] = useState(localStorage.getItem("token"));
  const [notas, setNotas] = useState([]);

  const handleLogin = (newToken) => {
    setToken(newToken);
  };

  const handleLogout = () => {
    localStorage.removeItem("token");
    setToken(null);
  };

  useEffect(() => {
    if (token) {
      axios
        .get("http://127.0.0.1:5000/notas", {
          headers: { Authorization: `Bearer ${token}` },
        })
        .then((res) => setNotas(res.data))
        .catch((err) => {
          console.error(err);
          handleLogout(); // token inválido ou expirado
        });
    }
  }, [token]);

  if (!token) {
    return <Login onLogin={handleLogin} />;
  }

  return (
    <div>
      <h2>Bem-vindo!</h2>
      <button onClick={handleLogout}>Sair</button>
      <h3>Suas Notas:</h3>
      <ul>
        {notas.map((nota, i) => (
          <li key={i}>{nota.texto || JSON.stringify(nota)}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
```

Nesse código, usamos o `useEffect` para fazer uma requisição para a rota de notas da API sempre que o token mudar. Se o token for inválido ou expirado, chamamos a função `handleLogout`, que remove o token do localStorage e atualiza o estado do aplicativo. Isso faz com que o componente de login seja exibido novamente. Perceba também que para fazer a requisição das notas, foi necessário passar o token de autenticação exatamente como fizemos no servidor JS.
```javascript
axios
  .get("http://127.0.0.1:5000/notas", {
    headers: { Authorization: `Bearer ${token}` },
  })
```
Nesse caso, o token é passado no cabeçalho da requisição, no campo `Authorization`, com o prefixo `Bearer`. Esse prefixo é uma convenção do padrão JWT e indica que o token é um token de acesso. O servidor deve verificar esse cabeçalho e validar o token antes de permitir o acesso aos dados protegidos.

## Segurança

O JWT é uma forma segura de autenticação, mas existem algumas maneiras de deixar a implementação ainda mais segura. Aqui estão algumas dicas:
- **Armazenamento do token**: O token deve ser armazenado de forma segura, para evitar que ele seja acessado por scripts maliciosos. O uso de cookies com a flag `HttpOnly` é uma boa prática nesse caso.
- **Validade do token**: O token deve ter um tempo de expiração definido, para evitar que ele seja usado indefinidamente. O JWT permite definir um tempo de expiração ao criar o token, e o servidor deve verificar esse tempo ao validar o token.
- **Revogação do token**: O servidor deve ter uma forma de revogar o token, caso o usuário faça logout ou o token seja comprometido. Uma forma de fazer isso é armazenar os tokens revogados em um banco de dados e verificar se o token está na lista de revogados ao validar o token.
- **HTTPS**: O uso de HTTPS é essencial para garantir a segurança da comunicação entre o cliente e o servidor. O HTTPS criptografa os dados transmitidos, evitando que eles sejam interceptados por terceiros.
- **CORS**: O CORS (Cross-Origin Resource Sharing) é um mecanismo de segurança que impede que scripts de um domínio acessem recursos de outro domínio. O uso do CORS é importante para evitar ataques de CSRF (Cross-Site Request Forgery), onde um script malicioso tenta fazer requisições para o servidor em nome do usuário. A biblioteca `flask-cors` já está configurada no código acima, mas é importante revisar as configurações para garantir que apenas os domínios autorizados possam acessar a API.
- **Deploy fechado**: Se a nossa API for exclusiva para o nosso aplicativo, podemos fechá-la para o mundo externo, permitindo apenas requisições do nosso domínio ou do IP do servidor onde está o Frontend. Isso pode ser feito configurando o firewall do servidor ou usando um proxy reverso, como o Nginx, para filtrar as requisições.





