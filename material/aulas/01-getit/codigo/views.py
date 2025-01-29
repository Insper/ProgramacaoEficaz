from utils import load_data, load_template, build_response
from urllib.parse import unquote_plus


def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        for chave_valor in corpo.split('&'):
            param = chave_valor.split('=')
            params[unquote_plus(param[0])] = unquote_plus(param[1])
        return build_response(code=303, reason='See Other', headers='Location: /')

    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    return build_response(load_template('index.html').format(notes=notes))
    # return load_template('index.html').format(notes=notes).encode()

