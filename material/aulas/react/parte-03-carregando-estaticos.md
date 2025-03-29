
Além de JavaScript e CSS, a nossa interface também precisa de algumas imagens. Elas podem ser adicionadas à pasta `public`. Faça o download da imagem do [logo do Get-it](img/logo-getit.png){:target="_blank"} e salve-o na pasta `public`. Agora a imagem estará disponível na rota `/logo-geti.png`. 

Vamos criar um novo componente para o `AppBar`. Crie o arquivo `src/components/AppBar/index.jsx` adicione o seguinte conteúdo:

```jsx
import "./index.css";

export default function AppBar() {
    return (
        <div className="appbar">
            <img src="/logo-getit.png" className="logo" />
            <span className="subtitle">Como o Post-it, mas com outro verbo</span>
        </div>
    );
}
```

Crie também o arquivo `src/components/AppBar/index.css` e adicione as classes CSS `appbar`, `logo` e `subtitle` abaixo:

```css
.appbar {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin: 0 0 2rem;
  padding: 10px 5px;
  background-color: #f7d736;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.19), 0 6px 6px rgba(0, 0, 0, 0.23);
}

.logo {
  height: 50px;
  margin-right: 1rem;
}

.subtitle {
  color: #2c2c2c;
}
```

Em seguida, modifique o arquivo src/App.jsx e adicione o componente `AppBar` no `App`:

```jsx hl_lines="4 18"
import axios from "axios";
import { useEffect, useState } from "react";
import Note from "./components/Note";
import AppBar from "./components/AppBar";
import "./App.css";

function App() {
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/notes/")
      .then((res) => setNotes(res.data));
  }, []);

  return (
    <>
      <AppBar />
      {notes.map((note) => (
        <Note key={`note__${note.id}`} title={note.title}>
          {note.content}
        </Note>
      ))}
    </>
  );
}

export default App;
```

## Adicionando mais classes CSS

Vamos adicionar a classe `card-container` para que as notas fiquem organizadas. Além disso, vamos adicionar também a classe `container`.

Altere o arquivo `src/App.css` adicionando as classes CSS `container` e `card-container` abaixo:

```css
.container {
  padding: 0 50px;
}

.card-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  place-content: space-evenly;
}
```

Além disso, atualize o arquivo `src/App.jsx`:

```jsx hl_lines="19 20 26 27"
import axios from "axios";
import { useEffect, useState } from "react";
import Note from "./components/Note";
import AppBar from "./components/AppBar";
import "./App.css";

function App() {
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/notes/")
      .then((res) => setNotes(res.data));
  }, []);

  return (
    <>
      <AppBar />
      <main className="container">
        <div className="card-container">
          {notes.map((note) => (
            <Note key={`note__${note.id}`} title={note.title}>
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


## Implementando a Criação de Anotações

Para continuar, avance para a próxima etapa.

[Implementando a Criação de Anotações](parte-04-criacao-notas.md){ .md-button .md-button--primary }