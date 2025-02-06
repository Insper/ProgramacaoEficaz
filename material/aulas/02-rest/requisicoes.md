# Como fazer requisição para seu webservice REST?

Responsável: Andre Pereira

### **Para que possamos fazer requisições para nosso webservice REST construído em python + flask usaremos a biblioteca requests.**

Para conseguir prosseguir com o tutorial é necessario instalar a biblioteca **“*requests"*** com o seguinte comando (recomendo criar uma .venv  [[tem tutorial aqui de como fazer isso]](../../auxiliar/venv.md))

```python
pip install requests
```

## Para começar vamos entender como a biblioteca requests funciona com os verbos HTTP:

```python
import requests # importa a biblioteca para dentro do seu arquivo

# ================================================================================================
# Dentro da biblioteca é possível fazer requisições com os principais verbos http disponíveis   
# ================================================================================================
# requests.delete(...args) --> DELETE
# requests.get(...args) --> GET
# requests.post(...args) --> POST
# requests.put(...args) --> PUT
```

## Para poder testar a biblioteca iremos utilizar o seguinte código em flask para simular uma API REST:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/test', methods=["GET"])
def hello_world_get():
    return jsonify({"message": "Tudo certo!"}), 200

@app.route('/test', methods=["DELETE"])
def hello_world_delete():
    req_data = request.get_json()

    if ("name" not in req_data):
        return jsonify({"message": "Erro!"}), 400

    return jsonify({"message": f"Olá {req_data['name']}!"}), 200

@app.route('/test', methods=["PUT"])
def hello_world_put():
    req_data = request.get_json()

    if ("name" not in req_data):
        return jsonify({"message": "Erro!"}), 400

    return jsonify({"message": f"Olá {req_data['name']}!"}), 200

@app.route('/test', methods=["POST"])
def hello_world_post():
    req_data = request.get_json()

    if ("name" not in req_data):
        return jsonify({"message": "Erro!"}), 400

    return jsonify({"message": f"Olá {req_data['name']}!"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5500)
```

## **Agora nós iremos fazer requisição para cada uma das rotas a cima**

### GET:

- Como primeiro parâmetro iremos passar a url para qual gostaríamos de fazer a requisição e depois passar de forma explicita o “headers” como um dicionário

```python
req = requests.get("http://localhost:5500/test", headers={})

# pega o json que foi retornado pela api 
res = req.json()
print(res) # {'message': 'Tudo certo!'}

# status retornado pelo nosso webservice REST em flask
print(req.status_code) # 200

```

### POST:

- Como primeiro parâmetro iremos passar a url para qual gostaríamos de fazer a requisição, depois passar de forma explicita o “headers” como um dicionário e por fim também iremos passar de forma explicita o parâmetro “json” como um dicionário que será o ***body/corpo*** da requisição

```python
req = requests.post("http://localhost:5500/test", headers={}, json={"name": "Andre"})

# status retornado pelo nosso webservice REST em flask
print(req.status_code) # 200

# pega o json que foi retornado pela api 
res = req.json() 
print(res) # {'message': 'Olá Andre!'}
```

### DELETE:

- Como primeiro parâmetro iremos passar a url para qual gostaríamos de fazer a requisição, depois passar de forma explicita o parâmetro “headers” como um dicionário e por fim também iremos passar de forma explicita o parâmetro “json” como um dicionário que será o ***body/corpo*** da requisição

```python
req = requests.post("http://localhost:5500/test", headers={}, json={"name": "Andre"})

print(req.status_code) # 200

# pega o json que foi retornado pela API 
res = req.json() 
print(res) # {'message': 'Olá Andre!'}
```

### PUT:

- Como primeiro parâmetro iremos passar a url para qual gostaríamos de fazer a requisição, depois passar de forma explicita o parâmetro “headers” como um dicionário e por fim também iremos passar de forma explicita o parâmetro “json” como um dicionário que será o ***body/corpo*** da requisição

```python
req = requests.put("http://localhost:5500/test", headers={}, json={"name": "Andre"})

# status retornado pelo nossa API
print(req.status_code) # 200

# pega o json que foi retornado pela API 
res = req.json() 
print(res) # {'message': 'Olá Andre!'}
```

## Consumindo uma API de terceiros

- Agora iremos consumir uma API que nos retorna dados sobre *pokémons*

### GET (https://pokeapi.co/api/v2/pokemon/ditto)

```python
req = requests.get("https://pokeapi.co/api/v2/pokemon/ditto", headers={})

print(req.status_code) # 200

res = req.json() 
print(res["abilities"]) # [{'ability': {'name': 'limber', 'url': 'https://pokeapi.co/api/v2/ability/7/'}, 'is_hidden': False, 'slot': 1}, {'ability': {'name': 'imposter', 'url': 'https://pokeapi.co/api/v2/ability/150/'}, 'is_hidden': True, 'slot': 3}]
```

- **Referências:**
    
    [Python's Requests Library (Guide) – Real Python](https://realpython.com/python-requests/)
    
    [PokéAPI](https://pokeapi.co/)