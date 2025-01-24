import json
from pathlib import Path


def extract_route(request):
    first_line = request.split('\n')[0]
    return first_line.split()[1][1:]


def read_file(filepath):
    with open(filepath, mode='rb') as f:
        return f.read()


def load_data(path):
    # with open(Path('data') / path) as f:
    with open(f'data/{path}') as f:
        return json.load(f)


def load_template(path):
    with open(f'templates/{path}') as f:
        return f.read()



def build_response(body='', code=200, reason='OK', headers=''):
    if headers:
        headers = '\n' + headers
    return f'HTTP/1.1 {code} {reason}{headers}\n\n{body}'.encode()
