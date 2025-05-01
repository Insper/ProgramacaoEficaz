# SSL Handshake - Como consertar o erro do PyMongo (MacOS)

Responsável: Andre Pereira

O seguinte erro pode ocorrer quando você estiver usando flask + flask_pymongo, principalmente em sistemas Mac:

```
pymongo.errors.ServerSelectionTimeoutError: SSL handshake failed: backendstore.documents.azure.com:10255: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:749)
```
 

Basta instalar pelo pip dentro da sua "venv” a biblioteca `certifi` e gerar o seguinte código na sua aplicação:

```python
import certifi
ca = certifi.where()
```

E na hora de se conectar com o mongo passar na instância do PyMongo o certificado pelo parâmetro `tlsCAFile` a variável `ca` que foi criada anteriormente

```python
from flask_pymongo import PyMongo, ObjectId
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["MONGO_URI"] = f"SUA_URL_DE_CONEXAO"
db = PyMongo(app, tlsCAFile=ca)
```

### **REFERÊNCIAS**:

[https://stackoverflow.com/questions/54484890/ssl-handshake-issue-with-pymongo-on-python3](https://stackoverflow.com/questions/54484890/ssl-handshake-issue-with-pymongo-on-python3)