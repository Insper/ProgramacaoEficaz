from flask import Flask, render_template_string, url_for
from utils import load_data


app = Flask(__name__)

NOTE_TEMPLATE = '''  <li>
    <h3>{title}</h3>
    <p>{details}</p>
  </li>
'''

RESPONSE_TEMPLATE = '''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Get-it</title>
</head>
<body>

<img src="{{{{ url_for('static', filename='img/logo-getit.png') }}}}">
<p>Como o Post-it, mas com outro verbo</p>

<ul>
{notes}
</ul>

</body>
</html>
'''

# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'

@app.route('/')
def index():
    notes_li = [
        NOTE_TEMPLATE.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    response = RESPONSE_TEMPLATE.format(notes=notes)

    return render_template_string(response)


if __name__ == '__main__':
    app.run(debug=True)
