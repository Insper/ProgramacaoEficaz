Para implementar a funcionalidade de edição de anotações, vamos precisar simular a navegação entre páginas. Para isso, vamos utilizar o [`react-router-dom`](https://reactrouter.com/en/main/start/tutorial){:target="_blank"}.

## Configuração Inicial

Para começar, instale o `react-router-dom` com o comando a seguir no terminal, dentro das pasta do projeto (notes-frontend):

```bash
npm install react-router-dom
```
Vamos utilizar o `react-router-dom` para criar um sistema de rotas para a nossa aplicação. Esta biblioteca nos permite definir rotas e renderizar componentes específicos para cada rota. Existem vários tipos de roteadores, mas vamos utilizar o `BrowserRouter` para criar um roteador que utiliza a API de histórico do navegador. 

- Abra o arquivo `src/main.jsx` e adicione as seguintes linhas de código:

```jsx hl_lines="3-6 10-15 19"
import React from 'react'
import ReactDOM from 'react-dom/client'
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import App from './App.jsx'
import './index.css'

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
```

A princípio, estamos definindo que ao acessar a rota `/`, queremos renderizar o componente `App`.
Nossa aplicação deve estar funcionando normalmente, sem alterações visíveis.


## Criando um componente para a edição de anotações

Vamos criar um componente novo para a página de edição. Crie um arquivo `src/components/Editar/index.jsx` com o seguinte conteúdo:

```jsx
export default function Editar() {
    return (
        <div className="App">
            <main className="container">
                <form className="form-card">
                    <input
                        className="form-card-title"
                        type="text"
                        name="titulo"
                    />
                    <textarea
                        className="autoresize"
                        name="detalhes"
                    ></textarea>
                    <button className="btn" type="submit">Criar</button>
                </form>
            </main >
        </div>
    );
}
```

O conteúdo é basicamente o formulário que já tínhamos na página principal. Porém vamos utilizá-lo para editar uma anotação.
Copie o arquivo de estilo `src/components/Formulario/index.css` para `src/components/Editar/index.css`.


## Definindo uma nova rota

Agora vamos definir uma nova rota para a página de edição. Queremos definir a rota `/edit/:noteId` para que possamos editar uma anotação específica.
Para isso, vamos atualizar o arquivo `src/main.jsx`:

```js hl_lines="8 16-19"
import React from 'react'
import ReactDOM from 'react-dom/client'
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import App from './App.jsx'
import Editar from './components/Editar'
import './index.css'

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
  {
    path: "edit/:noteId",
    element: <Editar />,
  },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
```

## Navegando para a página de edição

Vamos criar um link para navegar para a página de edição. Não vamos utilizar a tag html `<a>`, pois ao utilizar o elemento `a` o navegador irá recarregar a página. Nós não queremos isso, queremos apenas navegar entre as páginas utilizando os recursos do React. Para isso, vamos utilizar o componente `Link` do `react-router-dom`. 

Vamos atualizar o arquivo `src/components/Note/index.jsx`:


```jsx hl_lines="1 8"
import { Link } from "react-router-dom";
import "./index.css";

export default function Note(props) {
    return (
        <div className="card">
            <h3 className="card-title">{props.title}</h3>
            <Link to={`edit/${props.id}`}>✏️</Link>
            <div className="card-content">{props.children}</div>
        </div>
    );
}

```
Agora, ao clicar no botão de editar, vamos navegar para a página de edição através da rota `edit/noteID`.

## Envindo o ID da anotação para a página de edição

Vamos voltar para o arquivo `src/App.jsx` e adicionar um novo atributo `id` no componente `Note`:

```jsx hl_lines="28"
import axios from "axios";
import { useEffect, useState } from "react";
import Note from "./components/Note";
import AppBar from "./components/AppBar";
import Formulario from "./components/Formulario";
import "./App.css";

function App() {
  const [notes, setNotes] = useState([]);

  const carregaNotas = () => {
    axios
      .get("http://localhost:8000/api/notes/")
      .then((res) => setNotes(res.data));
  }

  useEffect(() => {
    carregaNotas();
  }, []);

  return (
    <>
      <AppBar />
      <main className="container">
        <Formulario loadNotes={carregaNotas} />
        <div className="card-container">
          {notes.map((note) => (
            <Note key={`note__${note.id}`} id={note.id} title={note.title}>
              {note.content}
            </Note>
          ))}
        </div>
      </main>
    </>
  );
}

export default App;
```

## Obtendo o ID da anotação

Ao acessar a página de edição, precisamos obter o ID da anotação da rota e fazer uma requisição para obter os dados da anotação.
O react-router-dom nos fornece uma ferramenta chamada loader que nos permite acessar os parâmetros da rota e carregar os dados necessários. 

Para isso, vamos importar o hook `useLoaderData` do `react-router-dom` e implementar uma função que receberá o ID da anotação informado na rota e fará uma requisição para obter os dados da anotação.

Na linha 13

```jsx hl_lines="2 5-10" 
import axios from "axios";
import { useLoaderData } from "react-router-dom";
import AppBar from "../AppBar";

export async function loader({ params }) {
    const note = await axios
                        .get(`http://localhost:8000/api/notes/${params.noteId}/`)
                        .then((response) => response.data)
    return { note };
}

export default function Editar() {

    return (
        <>
        <AppBar />
        <main className="container">
            <form className="form-card">
                <input
                    className="form-card-title"
                    type="text"
                    name="titulo"
                />
                <textarea
                    className="autoresize"
                    name="detalhes"
                ></textarea>
                <button className="btn" type="submit">Criar</button>
            </form>
        </main>
        </>
    );
}
```

## Usando a função loader

Definimos a função `loader`, mas precisamos realizar uma configuração para que ao acessar a rota `/edit/:noteId`, a função loader seja executada. Para isso, vamos atualizar o arquivo `src/main.jsx`:

```js hl_lines="8 19"
import React from 'react'
import ReactDOM from 'react-dom/client'
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import App from './App.jsx'
import Editar, { loader as noteLoader} from './components/Editar'
import './index.css'

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
  {
    path: "edit/:noteId",
    element: <Editar />,
    loader: noteLoader,
  },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
```

Estamos importando a função `loader` do arquivo `Editar` e definindo que ela deve ser executada ao acessar a rota `edit/:noteId`.

Voltando ao arquivo `src/components/Editar/index.jsx`, vamos utilizar o hook `useLoaderData` que chamará a função `loader` e vamos armazenar o retorno da função em uma variável `note`.


```jsx hl_lines="13" 
import axios from "axios";
import { useLoaderData } from "react-router-dom";
import AppBar from "../AppBar";

export async function loader({ params }) {
    const note = await axios
                        .get(`http://localhost:8000/api/notes/${params.noteId}/`)
                        .then((response) => response.data)
    return { note };
}

export default function Editar() {
    const { note } = useLoaderData();
    return (
        <>
        <AppBar />
        <main className="container">
            <form className="form-card">
                <input
                    className="form-card-title"
                    type="text"
                    name="titulo"
                />
                <textarea
                    className="autoresize"
                    name="detalhes"
                ></textarea>
                <button className="btn" type="submit">Criar</button>
            </form>
        </main>
        </>
    );
}
```



## Preenchendo o formulário com os dados da anotação

Agora que temos realizamos a requisição e armazenamos os dados da anotação na variável `note`, vamos preencher o formulário com os dados da anotação. 



```js hl_lines="3 15-16 27 32"
import axios from "axios";
import { useLoaderData } from "react-router-dom";
import { useState } from "react";
import AppBar from "../AppBar";

export async function loader({ params }) {
    const note = await axios
                        .get(`http://localhost:8000/api/notes/${params.noteId}/`)
                        .then((response) => response.data)
    return { note };
}

export default function Editar() {
    const { note } = useLoaderData();
    const [title, setTitle] = useState(note.title);
    const [content, setContent] = useState(note.content);
    
    return (
        <>
        <AppBar />
        <main className="container">
            <form className="form-card" onSubmit={salvarNota}>
                <input
                    className="form-card-title"
                    type="text"
                    name="titulo"
                    value={title}
                />
                <textarea
                    className="autoresize"
                    name="detalhes"
                    value={content}
                ></textarea>
                <button className="btn" type="submit">Criar</button>
            </form>
        </main>
        </>
    );
}
```

Ao acessar a página de edição, o formulário será preenchido com os dados da anotação.

!!! example "Exercício"
    Assim como fizemos na página de criação, vamos implementar a função `salvarNota` que será responsável por enviar os dados da anotação para a API.

    Agora fica por sua conta, implemente as etapas a seguir:

    - Quando os campos do formulário forem alterados, os estados `title` e `content` devem ser atualizados.
    - Implemente a função `salvarNota` que será responsável por enviar os dados da anotação para a API.
    - Ao clicar no botão de salvar, a função `salvarNota` deve ser chamada.
    - Após salvar a anotação, o usuário deve ser redirecionado para a página inicial. Para esta etapa, continue lendo a próxima seção.

## Redirecionando para a página inicial

Ao finalizar a edição da anotação, a nota deve estar sendo salva, porém o usuário não é redirecionado para a página inicial. Para isso, vamos utilizar a ferramenta `useNavigate` do `react-router-dom`, este recurso nos permite navegar entre as páginas da aplicação.

No arquivo `src/components/Editar/index.jsx`: 

- Importe o hook `useNavigate`;
- Crie uma variável `navigate` utilizando o hook `useNavigate`;
- O comando `navigate("/");` deve ser chamado após a atualização da anotação ser bem sucessida. Esta etapa você deve descobrir onde implementar.


```jsx hl_lines="2 14"
import axios from "axios";
import { useLoaderData, useNavigate } from "react-router-dom";
import { useState } from "react";
import AppBar from "../AppBar";

export async function loader({ params }) {
    const note = await axios
                        .get(`http://localhost:8000/api/notes/${params.noteId}/`)
                        .then((response) => response.data)
    return { note };
}

export default function Editar() {
    const navigate = useNavigate();
    const { note } = useLoaderData();
    const [title, setTitle] = useState(note.title);
    const [content, setContent] = useState(note.content);

  // O Restante do seu código
```

## Bônus: implementando a rotação dos cartões

Para continuar, avance para a próxima etapa.

[Bônus: implementando a rotação dos cartões](parte-06-bonus.md){ .md-button .md-button--primary }