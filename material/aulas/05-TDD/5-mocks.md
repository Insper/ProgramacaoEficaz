# **Entendendo e Usando Mocks no pytest**

## 📌 **O que são Mocks e por que usá-los?**  

Quando escrevemos testes, às vezes precisamos testar código que **depende de recursos externos**, como:  

✅ Chamadas a APIs externas.  
✅ Interações com arquivos ou sistemas de terceiros.  
✅ Funções que consomem muito tempo ou recursos.  

Esses componentes podem ser difíceis de testar diretamente porque:  
❌ **São lentos** – Uma API pode demorar segundos para responder.  
❌ **São imprevisíveis** – Um serviço externo pode estar fora do ar.  
❌ **Não queremos modificar dados reais** – Testar algo que pode afetar usuários reais pode ser perigoso.  

Para resolver isso, usamos **Mocks**.  


## 🔹 **O que é um Mock?**  

Um **Mock** é um objeto falso que **simula** o comportamento de um objeto real. Ele permite testar código **sem precisar da dependência real**.  

Em Python, podemos usar a biblioteca **`unittest.mock`**, que permite criar **Mocks** para substituir funções e objetos reais nos testes.  

✅ **Vantagens dos Mocks:**  
- Testamos apenas o código **que queremos validar**, sem depender de APIs, arquivos ou serviços externos.  
- Os testes ficam **rápidos**, pois não precisam esperar por respostas externas.  
- Podemos simular **diferentes cenários**, como erros ou respostas inesperadas.  

## 📌 **Exemplo inicial: Testando uma Função que Depende de Outra**  

### **Cenário:**

Temos uma função que depende de outra função para funcionar. Queremos testar a primeira função **sem chamar a segunda**.

### **Função Principal:**

```python
def funcao_secundaria(valor):
    """Função que a função principal depende."""
    return valor + 10

def funcao_principal(valor):
    """Depende de outra função para funcionar."""
    resultado = funcao_secundaria(valor)
    return resultado * 2
```

### **O problema:**

Quando testamos `funcao_principal`, **ela chama `funcao_secundaria` de verdade**. Se houver um problema em `funcao_secundaria`, nosso teste falhará, mesmo que `funcao_principal` esteja correta.

### **Solução: Usar um Mock para `funcao_secundaria`**

```python
from unittest.mock import patch

def test_funcao_principal():
    """Testa a função principal sem chamar a secundária."""
    
    # Criamos um Mock para funcao_secundaria
    with patch("__main__.funcao_secundaria") as mock_secundaria:
        # Definimos um comportamento falso para o mock
        mock_secundaria.return_value = 20
        
        # Agora, quando chamarmos a função principal, ela usará o Mock em vez da real
        resultado = funcao_principal(10)
        
        assert resultado == 40
```

### **Explicando o Código do Mock**

1. **`patch("__main__.funcao_secundaria")`** → Substitui temporariamente `funcao_secundaria` por um Mock.
2. **`mock_secundaria.return_value = 20`** → Simula o retorno da função secundária.
3. **Chamamos `funcao_principal(10)`**, mas agora **a função secundária não é chamada de verdade**.
4. **O teste verifica se a função retorna `40` como esperado.**

Faça um teste mudando a função `funcao_secundaria` para retornar outra coisa e veja se o teste continua funcionando.

## 📌 **Exemplo Prático: Testando uma Função que Faz Requisições HTTP**  

### **Cenário:**  
Temos uma função que obtém a previsão do tempo de uma API externa. Queremos testá-la **sem realmente chamar a API**.  

Se não usarmos Mocks, cada vez que rodarmos o teste, ele chamará a API de verdade, o que pode ser:  
❌ Lento (depende da resposta da API).  
❌ Instável (a API pode estar fora do ar).  
❌ Caro (se a API for paga).  

Com **Mocks**, podemos substituir a chamada real por uma **resposta simulada**, garantindo que o teste sempre rode rápido e previsível.  


### 🔹 **Passo 1: Criando a Função que Depende da API**  
Esta função faz uma requisição a uma API externa para obter a previsão do tempo.  

```python
import requests

def obter_previsao_tempo(cidade):
    """Consulta uma API externa para obter a previsão do tempo."""
    url = f"https://api.previsao-tempo.com/{cidade}"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        return resposta.json()["previsao"]
    else:
        return "Erro ao obter previsão"
```

### **O problema:**  
Quando testamos essa função, **ela faz uma requisição real para a API**. Queremos testá-la sem depender da API externa.  


### 🔹 **Passo 2: Criando um Mock para a Requisição**  

Usamos **Mocks** para substituir `requests.get()` por uma versão falsa que retorna sempre a mesma resposta.  

```python
from unittest.mock import patch

def test_obter_previsao_tempo():
    """Testa a função sem chamar a API de verdade."""
    
    # Criamos um Mock para requests.get
    with patch("requests.get") as mock_get:
        # Definimos um comportamento falso para o mock
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"previsao": "Ensolarado"}
        
        # Agora, quando chamarmos a função, ela usará o Mock em vez da API real
        resultado = obter_previsao_tempo("São Paulo")
        
        assert resultado == "Ensolarado"
```


## 🔹 **Explicando o Código do Mock**
### 🛠️ **O que o Mock está fazendo?**
1. **`patch("requests.get")`** → Substitui temporariamente `requests.get` por um Mock.  
2. **`mock_get.return_value.status_code = 200`** → Simula uma resposta bem-sucedida da API.  
3. **`mock_get.return_value.json.return_value = {"previsao": "Ensolarado"}`** → Simula o JSON retornado pela API.  
4. **Chamamos `obter_previsao_tempo("São Paulo")`**, mas agora **a API não é chamada de verdade**.  
5. **O teste verifica se a função retorna `"Ensolarado"` como esperado.**  


## 🔹 **Testando um Erro da API**
Podemos testar **diferentes cenários**, como a API retornando erro:  

```python
def test_obter_previsao_tempo_erro():
    """Testa o que acontece se a API falhar."""
    
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 500  # Simulamos um erro da API
        
        resultado = obter_previsao_tempo("São Paulo")
        
        assert resultado == "Erro ao obter previsão"
```

Agora garantimos que a função **lida corretamente com falhas na API**.


## 📌 **Resumo**
| **O que os Mocks fazem?** | **Vantagens** |
|----------------------------|--------------|
| Substituem funções ou objetos reais nos testes | Testes mais rápidos e previsíveis |
| Simulam diferentes respostas (sucesso, erro, timeout) | Testamos cenários difíceis de simular com código real |
| Evitam dependências externas como APIs ou arquivos | Testes independentes de servidores externos |

### **Quando usar Mocks?**
✅ Quando o código depende de **APIs externas**.  
✅ Quando queremos **simular erros** sem realmente causar falhas.  
✅ Quando precisamos **testar código que depende de outros códigos**.  