# Comandos úteis do Pytest

Sugestão de: Gabriel E. Vivacqua e Vitor H. Costa

O `pytest` possui diversas opções que ajudam a executar, filtrar e analisar testes.

A estrutura básica de execução é:

```bash
pytest
```

Esse comando procura automaticamente por arquivos e funções de teste no projeto.

Por exemplo, arquivos com nomes como:

```text
test_calculadora.py
calculadora_test.py
```

e funções como:

```python
def test_soma():
    assert 2 + 2 == 4
```

---

## Ver mais detalhes da execução

### `-v` ou `--verbose`

A opção `-v` (*verbose*) faz com que o `pytest` mostre mais informações durante a execução dos testes.

```bash
pytest -v
```

Sem `-v`, uma execução pode aparecer assim:

```text
...
3 passed
```

Com `-v`:

```text
test_calculadora.py::test_soma PASSED
test_calculadora.py::test_subtracao PASSED
test_calculadora.py::test_multiplicacao PASSED
```

Isso é especialmente útil para identificar **qual teste passou ou falhou**.

Também podemos executar um arquivo específico:

```bash
pytest test_calculadora.py -v
```

---

## Mostrar um resumo dos testes

### `-r`

A opção `-r` permite escolher quais tipos de resultados devem aparecer no **resumo final da execução**.

A sintaxe é:

```bash
pytest -r OPÇÕES
```

Por exemplo:

```bash
pytest -r f
```

mostra informações adicionais sobre os testes que falharam.

As principais opções são:

| Opção | Significado                                                   |
| ----- | ------------------------------------------------------------- |
| `f`   | `failed` — testes que falharam                                |
| `E`   | `error` — testes que tiveram erro durante a execução          |
| `s`   | `skipped` — testes que foram ignorados                        |
| `x`   | `xfailed` — testes que falharam como esperado                 |
| `X`   | `xpassed` — testes que deveriam falhar, mas passaram          |
| `p`   | `passed` — testes que passaram                                |
| `P`   | `passed with output` — testes que passaram e produziram saída |

É possível combinar várias opções:

```bash
pytest -r fs
```

Nesse caso, o resumo apresenta informações sobre testes que **falharam** e testes que foram **ignorados**.

Uma opção bastante útil é:

```bash
pytest -ra
```

O `a` significa mostrar informações sobre **todos os resultados relevantes**, exceto os testes que simplesmente passaram.

---

## Ver os comandos disponíveis

### `-h` ou `--help`

Mostra a lista de opções disponíveis no `pytest`.

```bash
pytest -h
```

ou:

```bash
pytest --help
```

Esse comando é útil quando você não lembra exatamente o nome ou funcionamento de alguma opção.

---

# Escolhendo quais testes executar

## Executar os testes de um arquivo específico

Para executar somente os testes presentes em um determinado arquivo:

```bash
pytest test_calculadora.py
```

Por exemplo, suponha que o projeto tenha:

```text
test_calculadora.py
test_usuario.py
test_produto.py
```

O comando:

```bash
pytest test_usuario.py
```

executará somente os testes presentes em `test_usuario.py`.

---

## Executar um teste específico

Podemos utilizar `::` para indicar exatamente qual teste queremos executar.

```bash
pytest arquivo_test.py::funcao_test
```

Por exemplo:

```python
def test_soma():
    assert 2 + 2 == 4


def test_subtracao():
    assert 5 - 2 == 3
```

Para executar somente `test_soma`:

```bash
pytest test_calculadora.py::test_soma
```

---

## Executar os testes de uma classe específica

Quando os testes estão organizados em classes, também podemos selecionar uma classe inteira.

Por exemplo:

```python
class TestCalculadora:

    def test_soma(self):
        assert 2 + 2 == 4

    def test_subtracao(self):
        assert 5 - 2 == 3
```

Para executar todos os testes da classe:

```bash
pytest test_calculadora.py::TestCalculadora
```

Para executar somente um método:

```bash
pytest test_calculadora.py::TestCalculadora::test_soma
```

---

## Selecionar testes pelo nome

### `-k`

A opção `-k` permite executar testes que possuem determinado texto em seu nome.

Por exemplo:

```bash
pytest -k soma
```

Considere os testes:

```python
def test_soma_inteiros():
    ...


def test_soma_decimais():
    ...


def test_subtracao():
    ...
```

O comando:

```bash
pytest -k soma
```

executará:

```text
test_soma_inteiros
test_soma_decimais
```

mas não executará:

```text
test_subtracao
```

Também podemos usar expressões:

```bash
pytest -k "soma or subtracao"
```

ou:

```bash
pytest -k "soma and not decimal"
```

---

# Controlando a execução

## Parar na primeira falha

### `-x`

A opção `-x` faz o `pytest` interromper a execução assim que encontrar o primeiro teste que falhou.

```bash
pytest -x
```

Isso pode ser útil quando você está corrigindo erros um de cada vez.

Por exemplo, se existem 100 testes e o terceiro falha, o `pytest` interrompe a execução imediatamente.

---

## Parar depois de uma quantidade de falhas

### `--maxfail`

Permite determinar quantas falhas podem acontecer antes de interromper a execução.

```bash
pytest --maxfail=2
```

Nesse exemplo, o `pytest` interrompe a execução depois que **dois testes falharem**.

Também é possível combinar com `-v`:

```bash
pytest -v --maxfail=2
```

---

## Executar novamente apenas os testes que falharam

### `--lf` ou `--last-failed`

O `pytest` guarda informações sobre a execução anterior.

O comando:

```bash
pytest --lf
```

executa somente os testes que falharam na última execução.

Por exemplo, se temos 50 testes e apenas dois falharam, depois de corrigir o código podemos executar:

```bash
pytest --lf
```

Assim, inicialmente somente esses dois testes serão executados novamente.

---

## Executar primeiro os testes que falharam anteriormente

### `--ff` ou `--failed-first`

Executa todos os testes, mas coloca primeiro aqueles que falharam na execução anterior.

```bash
pytest --ff
```

Isso é útil quando queremos verificar rapidamente se uma correção resolveu um problema, mas ainda queremos executar toda a suíte de testes.

---

# Controlando o que aparece no terminal

## Mostrar os `print()` dos testes

### `-s`

Por padrão, o `pytest` captura a saída produzida por `print()`.

Considere:

```python
def test_soma():
    print("Executando teste de soma")
    assert 2 + 2 == 4
```

Executando:

```bash
pytest
```

o texto normalmente não aparece durante um teste que passa.

Com:

```bash
pytest -s
```

veremos:

```text
Executando teste de soma
```

Essa opção pode ser útil durante a depuração.

Também é comum combinar:

```bash
pytest -v -s
```

---

## Mostrar menos informações

### `-q` ou `--quiet`

A opção `-q` (*quiet*) reduz a quantidade de informações mostradas pelo `pytest`.

```bash
pytest -q
```

É útil quando queremos uma saída mais curta, principalmente em projetos que possuem muitos testes.

---

# Controlando a mensagem de erro

## Alterar o formato do traceback

### `--tb`

Quando um teste falha, o `pytest` mostra o *traceback*, ou seja, informações indicando onde ocorreu o erro.

Podemos controlar a quantidade de informações mostradas.

### Traceback curto

```bash
pytest --tb=short
```

Mostra uma versão reduzida do erro.

### Traceback completo

```bash
pytest --tb=long
```

Mostra informações mais detalhadas.

### Apenas uma linha

```bash
pytest --tb=line
```

Mostra cada erro de forma bastante compacta.

### Não mostrar traceback

```bash
pytest --tb=no
```

Pode ser útil quando queremos visualizar apenas quais testes falharam.

Uma combinação bastante prática é:

```bash
pytest -v --tb=short
```

---

# Listando testes sem executá-los

## `--collect-only`

O `pytest` primeiro procura os testes existentes no projeto. Esse processo é chamado de **coleta de testes** (*test collection*).

Podemos pedir para ele mostrar quais testes encontrou sem executá-los:

```bash
pytest --collect-only
```

Por exemplo:

```text
test_calculadora.py
    test_soma
    test_subtracao
    test_multiplicacao
```

Esse comando é útil para verificar se o `pytest` está conseguindo encontrar todos os testes esperados.

Para uma saída mais compacta:

```bash
pytest --collect-only -q
```

---

# Executando testes marcados

## `-m`

O `pytest` permite adicionar **marcadores** (*markers*) aos testes.

Por exemplo:

```python
import pytest


@pytest.mark.lento
def test_operacao_complexa():
    assert True
```

Podemos executar apenas os testes que possuem a marca `lento`:

```bash
pytest -m lento
```

Também podemos excluir esses testes:

```bash
pytest -m "not lento"
```

Os marcadores são úteis para separar, por exemplo:

* testes rápidos;
* testes lentos;
* testes de integração;
* testes que dependem de banco de dados;
* testes que dependem de serviços externos.

> Marcadores personalizados normalmente devem ser registrados no arquivo de configuração do `pytest`.

---

# Algumas combinações úteis

As opções podem ser combinadas.

### Ver detalhadamente os testes

```bash
pytest -v
```

### Ver detalhes e os `print()`

```bash
pytest -v -s
```

### Parar na primeira falha

```bash
pytest -v -x
```

### Mostrar traceback mais curto

```bash
pytest -v --tb=short
```

### Executar novamente apenas os testes que falharam

```bash
pytest -v --lf
```

### Executar testes cujo nome contém `usuario`

```bash
pytest -v -k usuario
```

### Executar um teste específico

```bash
pytest test_calculadora.py::test_soma -v
```

---

# Resumo dos principais comandos

| Comando                    | Função                                         |
| -------------------------- | ---------------------------------------------- |
| `pytest`                   | Executa os testes encontrados                  |
| `pytest arquivo.py`        | Executa os testes de um arquivo                |
| `pytest arquivo.py::teste` | Executa um teste específico                    |
| `-v`                       | Mostra mais detalhes                           |
| `-q`                       | Mostra menos informações                       |
| `-s`                       | Exibe saídas de `print()`                      |
| `-r`                       | Controla o resumo da execução                  |
| `-k`                       | Filtra testes pelo nome                        |
| `-m`                       | Filtra testes por marcador                     |
| `-x`                       | Para na primeira falha                         |
| `--maxfail=N`              | Para após `N` falhas                           |
| `--lf`                     | Executa os testes que falharam anteriormente   |
| `--ff`                     | Executa primeiro os que falharam anteriormente |
| `--tb=short`               | Mostra um traceback reduzido                   |
| `--collect-only`           | Lista os testes sem executá-los                |
| `-h`                       | Mostra a ajuda do `pytest`                     |
