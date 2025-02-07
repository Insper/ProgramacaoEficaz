# Introdução ao **pytest**  

O **pytest** é um dos frameworks de teste mais populares para Python. Ele é simples de usar, mas poderoso o suficiente para escrever testes complexos. Com **pytest**, você pode testar funções, classes e até mesmo aplicações inteiras com facilidade.  

## O que é pytest?  

O **pytest** é um framework que facilita a escrita e execução de testes automatizados em Python. Ele é mais intuitivo do que o módulo padrão `unittest`, permitindo que você escreva testes com menos código e mais clareza.  

## Como instalar o pytest  

Para começar a usar o `pytest`, primeiro você precisa instalá-lo. **Dentro do ambiente virtual**, basta rodar:  

```sh
pip install pytest
```

Após a instalação, você pode verificar se o `pytest` está disponível com:  

```sh
pytest --version
```


## Como escrever um teste básico  

Os testes no `pytest` são escritos como funções normais e utilizam **assertivas (`assert`)** para verificar se os resultados são os esperados.  

### 📌 **Exemplo de um teste simples**  

Crie um arquivo chamado **`test_math.py`** e adicione o seguinte código:  

```python
def soma(a, b):
    return a + b

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0
```

Aqui, estamos testando se a função `soma(a, b)` retorna os valores corretos para diferentes entradas.  


## Como rodar os testes  

Para executar os testes, basta rodar o seguinte comando no terminal:  

```sh
pytest
```

Se tudo estiver correto, você verá uma saída semelhante a:  

```
============================= test session starts =============================
collected 1 item                                                               

test_math.py .                                                       [100%]

============================== 1 passed in 0.01s ==============================
```

Mas como o `pytest` sabe que o arquivo `test_math.py` contém testes? Ele segue uma convenção de nomenclatura: os arquivos de teste devem começar com `test_` ou terminar com `_test`. Por causa disso, não é comum que tenhamos testes e o código principal no mesmo arquivo.

O mais usual seria ter um arquivo `math.py` com a implementação da função `soma` e um arquivo `test_math.py` com os testes.

## Red-Green-Refactor

Para exemplificar o fluxo **Red-Green-Refactor** com `pytest`, vamos criar testes para uma função chamada `calcula_media` que deve receber uma lista de inteiros e retornar a média dos valores. Para isso, vamos seguir os seguintes passos:

1. Crie um arquivo `funcoes.py`.
2. Crie um arquivo chamado `test_funcoes.py`.

### 🔹 **Ciclo 1 - Criar a função de média**
#### **1️⃣ Red (Escrevemos um teste que falha)**  
Antes de criar a função, escrevemos um teste no arquivo `test_funcoes.py` para garantir que a média de `[2, 4, 6]` seja `4.0`:

```python
from funcoes import calcula_media
def test_calcula_media():
    assert calcula_media([2, 4, 6]) == 4.0
```

🚨 **O teste falha** porque `calcula_media` ainda não existe.

#### **2️⃣ Green (Fazemos o teste passar com o código mais simples possível)**  
Agora criamos a função **mais simples possível** no arquivo `funcoes.py` para passar no teste:

```python
def calcula_media(lista):
    total = 0
    for num in lista:
        total += num
    return total / len(lista)
```

✅ **Agora o teste passa!**

#### **3️⃣ Refactor (Melhoramos o código, se necessário)**  
Agora que saímos de DevLife, podemos utilizar as funções prontas do Python para simplificar o código:

```python
def calcula_media(lista):
    return sum(lista) / len(lista)
```

### 🔹 **Ciclo 2 - Lidar com listas vazias**
Agora, queremos melhorar a função para que **não quebre** caso receba uma lista vazia.

#### **1️⃣ Red (Escrevemos um novo teste que falha)**  
Adicionamos um novo caso de teste para listas vazias:

```python
def test_calcula_media_lista_vazia():
    assert calcula_media([]) == 0  # Esperamos que a média de uma lista vazia seja 0
```

🚨 **O teste falha!** O código atual gera um erro de **divisão por zero**.

#### **2️⃣ Green (Fazemos o teste passar com a solução mais simples possível)**  
Agora, alteramos a função para tratar listas vazias:

```python
def calcula_media(lista):
    if lista == []:
        return 0
    else:
        return sum(lista) / len(lista)
```

✅ **Agora o teste passa!**

#### **3️⃣ Refactor (Melhoramos a implementação)**  

A função funciona, mas podemos utilizar técnicas mais avançadas para simplificar o código:

```python
def calcula_media(lista):
    return 0 if lista == [] else sum(lista) / len(lista)
```

## 🔹 **Resumo do Processo**
🔴 **Red** – Criamos um teste antes da implementação e verificamos que ele falha.  
🟢 **Green** – Implementamos o código mais simples possível para fazer o teste passar.  
🛠️ **Refactor** – Melhoramos o código sem alterar o comportamento esperado.  

E qual é a melhor maneira de estruturarmos os testes? Vamos ver isso [a seguir!](2-boaspraticas.md)

<!-- ## Recursos úteis do pytest  

### 1️⃣ **Testes paramétricos** (rodar o mesmo teste com vários valores)  
Podemos usar `@pytest.mark.parametrize` para testar múltiplos casos de forma eficiente:  

```python
import pytest

@pytest.mark.parametrize("a, b, resultado", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_soma(a, b, resultado):
    assert soma(a, b) == resultado
```

### 2️⃣ **Testes com exceções** (testando erros)  
Podemos verificar se uma função levanta uma exceção esperada com `pytest.raises()`:  

```python
import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não permitida!")
    return a / b

def test_divide():
    with pytest.raises(ValueError):
        divide(1, 0)
```

### 3️⃣ **Rodando apenas um teste específico**  
Se quiser rodar apenas um teste específico, use:  

```sh
pytest test_math.py::test_soma
```

### 4️⃣ **Obter um relatório mais detalhado**  
Para ver mensagens detalhadas sobre os testes, use a opção `-v`:  

```sh
pytest -v
```


## Conclusão  

O `pytest` é uma ferramenta essencial para quem quer escrever testes de forma simples e eficiente em Python. Com uma sintaxe intuitiva e diversas funcionalidades úteis, ele facilita a criação e execução de testes automatizados, garantindo que seu código funcione corretamente.  

Agora que você conhece o básico, experimente escrever seus próprios testes e explorar mais recursos do `pytest`! 🚀 -->