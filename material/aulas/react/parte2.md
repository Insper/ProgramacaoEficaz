# Continuação

## Implementando a edição de anotações
Para a edição de anotações precisamos implementar uma página nova. Para isso, vamos utilizar o componente `Route` do `react-router-dom`. Para instalar o `react-router-dom` execute o comando:

        npm install react-router-dom

Para mais detalhes visite: [https://reactrouter.com/en/main/start/overview](https://reactrouter.com/en/main/start/overview)

## Configuração Inicial

Faça as seguintes atualizações no arquivo `src/index.js`:

Vamos utilizar o React Router para definir qual componente devemos renderizar dependendo da rota.

A princípio estamos definindo que ao acessar a rota `/` queremos renderizar o componente `App`.

```js hl_lines="6 8-13 18"
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  }
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
```

## Criando a página de edição

Vamos criar um componente novo para a página de edição. Crie um arquivo `src/components/Edit/index.js` com o seguinte conteúdo:

```js
export default function Edit() {
    return (
        <div className="App">
            <main className="container">
                <form className="form-card" method="post">
                    <input
                        className="form-card-title"
                        type="text"
                        name="titulo"
                        placeholder="Título"
                    />
                    <textarea
                        className="autoresize"
                        name="detalhes"
                        placeholder="Digite o conteúdo..."
                    ></textarea>
                    <button className="btn" type="submit">Criar</button>
                </form>
            </main >
        </div>
    );
}
```

O conteúdo é basicamente o formulário que já tínhamos na página principal. Porém vamos utilizá-lo para editar uma anotação.

## Definindo uma nova rota

Agora vamos definir uma nova rota para a página de edição. Queremos definir a rota `/edit/:noteId` para que possamos editar uma anotação específica.
Para isso, vamos atualizar o arquivo `src/index.js`:

```js hl_lines="7 14-17"
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import Edit from './components/Edit';

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
  {
    path: "edit/:noteId",
    element: <Edit />,
  }
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
```

## Navegando para a página de edição

Vamos criar um link para navegar para a página de edição. Não vamos utilizar a tag html `#!html<a>`, vamos utilizar o componente `Link` do `react-router-dom`. 

Para isso, vamos atualizar o arquivo `src/components/Note/index.js`:


```js hl_lines="2 26-38"
import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "./index.css";

function randomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function randomColor(){
    const cores = ["#ead3a7", "#9de0f5", "#ef89ba", "#fae890", "#abe9c1"]
    const indice = randomInt(0, cores.length - 1);
    return cores[indice];
}

export default function Note(props) {
    const [rotation, setRotation] = useState(0);
    useEffect(() => {
        setRotation(randomInt(-5, 5));
    }, []);

    const style = { transform: `rotate(${rotation}deg)`, backgroundColor: randomColor() };

    return (
        <div className="card" style={style}>
            <div className="card-action">
                <h3 className="card-title">{props.title}</h3>
                <div className="icons">
                    <div>
                        <Link to={`edit/${props.id}`}>
                            <i className="fas fa-edit"></i>
                        </Link>
                    </div>
                </div>
            </div>
            <div className="card-content">{props.children}</div>
        </div>
    );
}
```
<div style="width: 50%; margin-left:10rem;">
  ![Imagem de um card](../09-react/card.png)
</div>

Para utilizar um ícone de excluir foi utilizado o [Font Awesome](https://fontawesome.com/). Adicione o código abaixo dentro da tag `#!html <head>` do arquivo `public/index.html`:

```html
<script src="https://kit.fontawesome.com/7ae3e92237.js" crossorigin="anonymous"></script>
```

Adicione também o seguinte estilo no arquivo `src/components/Note/index.css`:

```css

.card-action {
    display: flex;
    justify-content: space-between;
}

.icons {
    display: flex;
}

```

Agora, ao clicar no botão de editar, vamos navegar para a página de edição através da rota `edit/noteID`.

## Obtendo o ID da anotação

Para obter o ID da anotação, vamos utilizar o `useParams` do `react-router-dom`. Para isso, vamos atualizar o arquivo `src/components/Edit/index.js`:

```js hl_lines="2 6"
import React from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

export default function Edit() {
    const { noteId } = useParams();

    return (
        <div className="App">
            <main className="container">
                <form className="form-card" method="post">
                    <input
                        className="form-card-title"
                        type="text"
                        name="titulo"
                        placeholder="Título"
                    />
                    <textarea
                        className="autoresize"
                        name="detalhes"
                        placeholder="Digite o conteúdo..."
                    ></textarea>
                    <button className="btn" type="submit">Criar</button>
                </form>
            </main >
        </div>
    );
}
```

!!! example "Exercício"
    Tente implementar o restante do componente para finalizar a edição de anotações. 







