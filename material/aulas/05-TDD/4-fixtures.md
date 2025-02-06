# **Entendendo e Usando Fixtures no pytest**

## 📌 **O que são Fixtures e por que usá-las?**  

Quando escrevemos testes, frequentemente precisamos **preparar um ambiente de teste** antes de rodá-los. Isso pode envolver a criação de objetos, a configuração de variáveis ou a inicialização de serviços.  

Podemos fazer isso dentro de cada teste, mas isso **gera código repetitivo**. Para evitar essa repetição e tornar os testes mais organizados, usamos **Fixtures** no `pytest`.  

## 🔹 **O que é uma Fixture?**  

No `pytest`, uma **Fixture** é uma função especial que:  
- **Configura um ambiente de teste antes do teste rodar**.  
- **Fornece dados ou objetos necessários para o teste**.  
- **Pode incluir código de limpeza (teardown) para rodar após o teste**.  

### **Vantagens das Fixtures:**  
✅ Evita repetição de código entre testes.  
✅ Facilita a manutenção, pois todas as configurações ficam centralizadas.  
✅ Torna os testes mais organizados e modulares.  
✅ Pode ser configurada para rodar automaticamente em vários testes.  

## 📌 **Exemplo Prático: Testando um Sistema de Pedidos**  

### **Cenário:**  
Temos um sistema que gerencia pedidos de um restaurante. Cada pedido tem um nome do cliente, uma lista de itens e um status (`"pendente"`, `"em preparo"` ou `"entregue"`).  

Queremos testar a funcionalidade de:  
1. Criar pedidos.  
2. Alterar o status do pedido.  

Se não usarmos Fixtures, teríamos que criar objetos de pedido **manualmente em cada teste**. Isso tornaria o código repetitivo.  

Com Fixtures, podemos criar automaticamente um pedido de teste antes de cada teste rodar.  


## 🔹 **Passo 1: Criando a Fixture**  
Aqui, criamos uma Fixture chamada `pedido_teste` que retorna um **pedido pronto para ser usado nos testes**.

No arquivo `pedidos.py`, temos a classe `Pedido` que representa um pedido do restaurante:
```python
class Pedido:
    def __init__(self, cliente, itens):
        self.cliente = cliente
        self.itens = itens
        self.status = "pendente"

    def atualizar_status(self, novo_status):
        self.status = novo_status
```

Agora, vamos criar a Fixture no arquivo `test_pedidos.py`:

```python
import pytest

@pytest.fixture
def pedido_teste():
    """Cria um pedido de teste antes de cada teste rodar."""
    return Pedido(cliente="João", itens=["Pizza", "Suco"])
```

### **O que acontece aqui?**  
🔹 Criamos a classe `Pedido`, que contém um cliente, itens e um status inicial como `"pendente"`.  
🔹 Criamos uma Fixture chamada `pedido_teste`, que **retorna um pedido pronto** para ser usado nos testes.  
🔹 Como essa Fixture será chamada antes de cada teste, evitamos **repetição de código** nos testes.  


## 🔹 **Passo 2: Usando a Fixture nos Testes**  
Agora podemos usar `pedido_teste` simplesmente passando-a como argumento nas funções de teste.

```python
def test_criacao_pedido(pedido_teste):
    """Testa se um pedido é criado corretamente."""
    assert pedido_teste.cliente == "João"
    assert pedido_teste.itens == ["Pizza", "Suco"]
    assert pedido_teste.status == "pendente"

def test_atualizar_status_pedido(pedido_teste):
    """Testa se conseguimos atualizar o status do pedido."""
    pedido_teste.atualizar_status("em preparo")
    assert pedido_teste.status == "em preparo"
```

### **O que acontece aqui?**  
✅ Em **`test_criacao_pedido`**, verificamos se o pedido foi criado corretamente.  
✅ Em **`test_atualizar_status_pedido`**, testamos se conseguimos mudar o status do pedido corretamente.  

### **Por que usar a Fixture aqui?**  
Sem a Fixture, precisaríamos criar um novo `Pedido` em cada teste, assim:  

```python
def test_criacao_pedido():
    pedido = Pedido(cliente="João", itens=["Pizza", "Suco"])
    assert pedido.cliente == "João"
    assert pedido.itens == ["Pizza", "Suco"]
    assert pedido.status == "pendente"

def test_atualizar_status_pedido():
    pedido = Pedido(cliente="João", itens=["Pizza", "Suco"])
    pedido.atualizar_status("em preparo")
    assert pedido.status == "em preparo"
```

Isso **repetiria o código de criação do pedido** em cada teste.  

Com a **Fixture**, garantimos que o objeto de teste sempre existe e está pronto antes dos testes rodarem.  


## 📌 **Passo 3: Melhorando a Fixture com múltiplos pedidos**  
Se quisermos testar diferentes pedidos, podemos modificar a Fixture para **receber parâmetros** e criar pedidos com diferentes clientes e itens.  

```python
@pytest.fixture
def pedido_teste(request):
    """Cria um pedido com diferentes valores, dependendo do teste."""
    cliente, itens = request.param
    return Pedido(cliente=cliente, itens=itens)
```

Agora, podemos criar múltiplos pedidos sem duplicar código:  

```python
import pytest

@pytest.mark.parametrize("pedido_teste", [
    ("João", ["Pizza", "Suco"]),
    ("Maria", ["Hambúrguer", "Refrigerante"]),
    ("Carlos", ["Salada", "Água"])
], indirect=True)
def test_atualizar_status_pedido(pedido_teste):
    pedido.atualizar_status("em preparo")
    assert pedido.status == "em preparo"
```

Agora testamos **vários pedidos diferentes** sem precisar criar cada um manualmente! O argumento `indirect=True` indica que os dados devem ser passados para a Fixture, e não para a função de teste diretamente.


## 🔹 **Resumo**
| **O que as Fixtures fazem?** | **Vantagens** |
|------------------------------|--------------|
| Criam objetos de teste automaticamente antes de cada teste | Evita código repetitivo |
| Permitem configurar e limpar recursos | Facilita a manutenção |
| Melhoram a organização dos testes | Código mais limpo e reutilizável |

### **Quando usar Fixtures?**  
- Quando um mesmo objeto ou configuração é necessária para vários testes.  
- Quando precisamos configurar um ambiente antes de testar.  
- Quando queremos manter os testes organizados e fáceis de modificar.  

Aqui complicou um pouco, mas não se preocupe! Se precisar, levante, tome uma água e releia o que não ficou claro. Depois de relaxar um pouco, vamos falar um pouco sobre o [próximo conteúdo](5-mocks.md).