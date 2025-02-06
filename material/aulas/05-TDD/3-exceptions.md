# Lidando com exceções

Em Python, exceções são erros que ocorrem durante a execução de um programa. Elas podem ser causadas por diversos motivos, como divisão por zero, acesso a índices inválidos em listas ou dicionários, entre outros. Quando uma exceção é lançada, o programa interrompe sua execução e tenta encontrar um bloco de código que a trate.

## Gerando exceções

Execute o código abaixo e veja qual a exceção gerada:

```python
lista = [1, 2, 3]
print(lista[3])
```

Executar esse código deve fazer aparecer a seguinte mensagem no terminal:

```terminal
IndexError: list index out of range
```

A exceção `IndexError` é lançada quando tentamos acessar um índice inexistente em uma lista. Acredito que já tenham visto essa exceção antes, não é mesmo? Além da exceção, o Python também exibe uma mensagem de erro que nos ajuda a entender o que aconteceu. Nesse caso, a mensagem diz que o índice está fora do alcance da lista.

Da mesma maneira que o Python exibe mensagens de erro, nós também podemos gerar nossas próprias exceções. Isso é útil quando queremos sinalizar que algo deu errado em nosso código. Por exemplo, podemos criar uma exceção personalizada para indicar que um valor inválido foi passado para uma função:

```python
def divide(a, b):
    if b == 0:
        raise Exception("Divisão por zero!")
    return a / b
```

Chamar essa função com `divide(10, 0)` resultará na seguinte exceção:

```terminal
Exception: Divisão por zero!
```

## Testando exceções

Se queremos que nossa função lance uma exceção em determinadas situações, precisamos testar se ela realmente faz isso. Para isso, podemos usar o método `pytest.raises()` do Pytest. Esse método verifica se uma exceção específica é lançada durante a execução de um bloco de código.

Vamos criar um teste para a função `divide()` que verifica se ela lança uma exceção `Exception` quando tentamos dividir por zero:

```python
import pytest

def test_divide_por_zero_gera_exception():
    with pytest.raises(Exception):
        # Given
        a = 10
        b = 0
        # When
        solucao = divide(a, b)
        # Then
        assert solucao
```

Nesse teste, utilizamos o bloco `with pytest.raises(Exception):` para verificar se a função `divide()` lança uma exceção do tipo `Exception`. Se a exceção for lançada, o teste passa. Caso contrário, ele falha.

## Se recuperando de exceções

Até hoje, toda vez que uma exceção era lançada, o programa parava de executar. Isso acaba sendo um grande problema quando um usuário está usando seu programa. Geralmente queremos evitar que o usuário perca o que está fazendo por conta de um problema isolado em alguma função.

Para isso, podemos usar o bloco `try`/`except` para capturar exceções e tratar erros de forma mais elegante. Veja o exemplo abaixo:

```python
def divide(a, b):
    if b == 0:
        raise Exception("Divisão por zero!")
    return a / b 

a = int(input("Digite um número"))
b = int(input("Digite outro número"))

while True:
    try:
        resultado = divide(a,b)
        print(f"O resultado da divisão é {resultado}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
```

Neste momento você pode estar pensando: "Eu não poderia simplesmente colocar um if antes de chamar a função?". A resposta seria Sim!, um if resolveria o problema nesse cenário. Geralmente queremos usar o bloco `try`/`except` quando existem muitos cenários possíveis que vão gerar erros e não queremos ou não podemos prever todos eles.

Agora que estamos pegando o jeito, vamos para os [tópicos mais avançados](4-fixtures.md).