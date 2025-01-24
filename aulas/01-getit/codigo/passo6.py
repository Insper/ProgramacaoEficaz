from flask import Flask, request

app = Flask(__name__)

RESPONSE_TEMPLATE = '''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Get-it</title>
</head>
<body>

<img src="img/logo-getit.png">
<p>Como o Post-it, mas com outro verbo</p>

<ul>
  <li>
    <h3>Receita de miojo</h3>
    <p>Bata com um martelo antes de abrir o pacote. Misture o tempero, coloque em uma vasilha e aproveite seu snack :)</p>
  </li>
  <li>
    <h3>Pão doce</h3>
    <p>Abra o pão e coloque o seu suco em pó favorito.</p>
  </li>
  <li>
    <h3>Sorvete com cristais de leite</h3>
    <p>Sirva o seu sorvete favorito em uma vasilha e jogue leite em cima.</p>
  </li>
  <li>
    <h3>Iogurte natural</h3>
    <p>Deixe o leite fora da geladeira (esse é mentira, não faça isso).</p>
  </li>
  <li>
    <h3>Homer Simpson</h3>
    <p>~( 8(|)</p>
  </li>
  <li>
    <h3>Numero mágico</h3>
    <p>142857</p>
  </li>
  <li>
    <h3>Série da Fundação - Isaac Asimov</h3>
    <p>É boa, leia.</p>
  </li>
</ul>

</body>
</html>
'''

@app.route('/')
def index():
    print(request.method)
    print(request.headers)

    return RESPONSE_TEMPLATE


if __name__ == '__main__':
    app.run(debug=True)
