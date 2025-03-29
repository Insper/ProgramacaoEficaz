
Para implementar a rotação dos cartões vamos utilizar novamente o `useEffect` e o `useState`. Modifique o `src/componentes/Note/index.jsx`:

```jsx hl_lines="2 5-9 12-17 20"
import { Link } from "react-router-dom";
import { useEffect, useState } from "react";
import "./index.css";

function randomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

export default function Note(props) {
  const [rotation, setRotation] = useState(0);
  useEffect(() => {
    setRotation(randomInt(-5, 5));
  }, []);

  const style = { transform: `rotate(${rotation}deg)` };

  return (
      <div className="card" style={style}>
          <h3 className="card-title">{props.title}</h3>
          <Link to={`edit/${props.id}`}>✏️</Link>
          <div className="card-content">{props.children}</div>
      </div>
    );
}
```

No exemplo acima, a função `randomInt` gera um número aleatório entre -5 e 5. A função `useEffect` é utilizada para definir o estado inicial de `rotation` com um valor aleatório.

Ao acessar a aplicação, os cartões devem estar rotacionados de forma aleatória.

## Adicionando as cores

Vamos utilizar a mesma ideia adotada na etapa anterior, para isso:

- Crie um array com as possíveis cores para os cartões. 
    
    - `#!js ["#ead3a7",  "#9de0f5",  "#ef89ba",  "#fae890",  "#abe9c1"]`

- Crie um estado para armazenar a cor do cartão.
- Utilize o `useEffect` para sortear uma cor aleatória para o cartão e atualize o estado com essa cor.
- Adicione uma chave `#!js "background-color"` no objeto `style` para aplicar a cor ao cartão.

Após realizar essas alterações, as cores devem ser aplicadas aos cartões de forma aleatória. :clap: :clap: :clap:

 