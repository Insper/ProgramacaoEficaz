from flask import Flask, render_template_string, url_for
from utils import load_data, load_template

app = Flask(__name__)

# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'

@app.route('/')
def index():
    notes_li = [
        load_template('components/note.html').format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    response = load_template('index.html').format(notes=notes)

    return render_template_string(response)


if __name__ == '__main__':
    app.run(debug=True)
