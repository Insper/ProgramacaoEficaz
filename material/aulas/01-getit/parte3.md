# 01 - Get-it - O retorno

## Parte 3: Separando algumas responsabilidades

O nosso código já está ficando grande e ele não faz quase nada! Um dos motivos para isso é a falta de coesão desse arquivo: esse arquivo possui a string HTML da página, que por sua vez contém todos os dados das anotações disponíveis, além do código que trata as conexões, requisições e respostas. Imagine o que aconteceria com uma quantidade razoável de anotações!

Essas três responsabilidades acumuladas no mesmo arquivo estão relacionadas a um conceito chamado <b>M</b>odel, <b>V</b>iew, <b>C</b>ontroller (MVC). Vocês tiveram um breve contato com esse conceito semestre passado, mas nós discutiremos mais a respeito em um futuro próximo.

### Modelo

Vamos começar separando a responsabilidade do modelo (lista de anotações) da responsabilidade de visualização (string HTML). Para isso, vamos criar uma lista de dicionários que contém os dados das anotações e a string HTML será gerada dinamicamente a partir desses dados:

```python hl_lines="2 7-11 21 37-45"
--8<-- "01-getit/codigo/passo8.py"
```

Você também vai precisar do arquivo [`notes.json` (clique aqui para baixar)](codigo/data/notes.json). Coloque-o em uma pasta chamada `data` dentro da pasta `static`.:

```
- DIRETORIO-DO-SEU-SERVIDOR
  |- servidor.py
  |- static
    |- data
      |- notes.json
    |- img
      |- logo-getit.png
```

!!! example "EXERCÍCIO"
    Crie um arquivo `utils.py` e implemente a função `#!python load_data`, que recebe o nome de um arquivo JSON e devolve o conteúdo do arquivo carregado como um objeto Python (A função deve assumir que este arquivo JSON está localizado dentro da pasta `static/data`). Por exemplo: se o conteúdo do arquivo `static/data/dados.json` for a string `{"chave": "valor"}`, sua função deve devolver o dicionário Python `#!python {"chave": "valor"}` para a entrada `dados.json` (note que o nome da pasta não é enviado como argumento). Dica: já existe uma [função Python para isso](https://docs.python.org/3/library/json.html).


!!! question choice
    No código anterior, estamos utilizando formatação de `string` um pouco diferente do que aprendemos em DevLife.

    Vamos ver como utilizar o método `.format`
    Considere o código a seguir:
    
    ```python
    x = 3
    y = 4
    z = x * y
    texto = 'O retângulo de lados {0} e {1} tem área {2}'

    print(texto.format(x, y, z))
    ``` 
       
    Escolha o será impresso no terminal:

    - [ ] O retângulo de lados {0} e {1} tem área {2}
    - [ ] O retângulo de lados 0 e 1 tem área 2
    - [X] O retângulo de lados 3 e 4 tem área 12
    - [ ] O retângulo de lados 4 e 3 tem área 12

    !!! details "Resposta"
        Será impresso `O retângulo de lados 3 e 4 tem área 12`, pois o método `.format` substituirá os valores entre chaves de acordo com a ordem em que os argumentos `x`, `y` e `z` foram passados. Para mais detalhes acesse: https://docs.python.org/3/tutorial/inputoutput.html#the-string-format-method

!!! question choice
    No código do servidor, utilizamos o método `.format` de outra maneira possível.
    A maneira utilizada é similar ao código a seguir:
    
    
    ```python
    print('This {food} is {adjective}.'.format(adjective='absolutely horrible', food='spam'))
    ``` 
       
    Escolhe o será impresso no terminal:

    - [X] This spam is absolutely horrible.
    - [ ] This {food} is {adjective}.
    - [ ] This absolutely horrible is spam.
    - [ ] This food is adjective.

    !!! details "Resposta"
        Será impresso `This spam is absolutely horrible.`, pois o método `.format` substituirá os valores entre chaves de acordo com os nomes utilizados `food` e `adjective`. Para mais detalhes acesse: https://docs.python.org/3/tutorial/inputoutput.html#the-string-format-method

!!! example "EXERCÍCIO"
      Tente reescrever o trecho de código abaixo utilizando o loop `#!python for`.
      Caso não esteja familiarizado com `list-comprehensions` acesse: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

      ```python
      # Cria uma lista de <li>'s para cada anotação
      # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
      notes_li = [
         NOTE_TEMPLATE.format(title=dados['titulo'], details=dados['detalhes'])
         for dados in load_data('notes.json')
      ]
      notes = '\n'.join(notes_li)

      response = RESPONSE_TEMPLATE.format(notes=notes).encode()
      ```

Perceba que a linha contendo a imagem foi alterada e foram adicionadas chaves. Isso acontece porque o método `format` do Python espera que as chaves sejam substituídas por valores. Como não queremos substituir essas chaves, precisamos dizer ao Python que elas são literais. Para isso, basta duplicar as chaves, ou seja, substituir `{` por `{{` e `}` por `}}`.

### Visualização

Ufa, já está um pouco melhor. Se quisermos adicionar mais anotações basta modificar o arquivo `notes.json`. Lembra da ideia de mantermos um baixo acoplamento? Aqui nós conseguimos melhorar esse ponto. Se eu quero adicionar mais dados eu só modifico o arquivo de dados (`notes.json`) e nenhum outro. O resto do código é independente disso.

Mas ainda dá para melhorar. Vamos refatorar um pouco mais o nosso código, separando a responsabilidade de visualização (HTML). 

!!! example "EXERCÍCIO"
    Crie uma pasta chamada `templates` dentro da pasta `static` e crie dentro dela um arquivo `index.html` com o conteúdo da string `#!python RESPONSE_TEMPLATE`. Não coloque aspas entorno do html.
    
    Ainda dentro da pasta `templates`, crie outra pasta chamada `components` e dentro dessa nova pasta um arquivo `note.html` com o conteúdo da string `#!python NOTE_TEMPLATE`. 


A sua estrutura de arquivos agora deve ser:

```
- DIRETORIO-DO-SEU-SERVIDOR
  |- servidor.py
  |- utils.py
  |- static
    |- data
      |- notes.json
    |- img
      |- logo-getit.png
    |- templates
        |- index.html
        |- components
            |- note.html
```

!!! example "EXERCÍCIO"
    Implemente a função `#!python load_template` no arquivo `utils.py` que recebe o nome de um arquivo de template e devolve uma string com o conteúdo desse arquivo. O nome do arquivo não inclui o nome da pasta `templates`. Por exemplo: para a entrada `index.html` você deve carregar o conteúdo do arquivo `static/templates/index.html`.

Vamos atualizar o código do servidor:

```python hl_lines="2 12 17"
--8<-- "01-getit/codigo/passo9.py"
```

### Controle de rotas

O código do servidor ainda possui duas responsabilidades diferentes: decidir qual rota seguir e o que fazer em cada rota (o que pode ser tão complexo quanto se queira). Vamos separar a responsabilidade de cada rota em uma função diferente:

```python hl_lines="2 13"
--8<-- "01-getit/codigo/passo10.py"
```

Você também vai precisar criar o arquivo `views.py` com o seguinte conteúdo (note que é exatamente o mesmo código que estava na função `index` do arquivo `servidor.py`):

```python
from utils import load_data, load_template

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)
```

Agora o nosso código está pronto para a [parte 4 do handout!](parte4.md)
