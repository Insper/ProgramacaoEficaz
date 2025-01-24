import utils

import unittest
import json
from unittest.mock import patch, mock_open
from pathlib import Path


REQUEST_TEMPLATE = '''{method} {route} HTTP/1.1
Host: 192.168.15.14:8080
Connection: keep-alive
Save-Data: on
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Linux; Android 11; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'''

def error_message(msg):
    marker = '\033[91m'
    end_marker = '\033[0m'
    return f'\n{marker}{msg}{end_marker}\n'


def target_function(function_name):
    def decorate(clazz):
        if hasattr(utils, function_name):
            return clazz
        print(
            f'\033[91mA função {function_name} não foi implementada, portanto não é possível testá-la.\033[0m')
        return None
    return decorate


@target_function('extract_route')
class ExtractRouteTestCase(unittest.TestCase):
    def assert_result(self, request, expected):
        msg = f'Algo deu errado! A rota extraída do request:\n"{request}"\n\ndeveria ser "{expected}"\n'

        try:
            obtido = utils.extract_route(request)
        except Exception as e:
            msg += 'Para o cenário indicado acima, a solução gera o seguinte erro:\n'
            msg += f'\n{type(e).__name__}: {e}'
            self.assertTrue(False, msg=error_message(msg))

        self.assertIsInstance(obtido, str, msg=error_message(
            f'{msg}\nEra esperado que o retorno fosse uma string, mas foi o tipo {type(obtido).__name__}. Obtido: {obtido}'))

        msg += f'Obtido "{obtido}"'
        self.assertEqual(expected, obtido, msg=error_message(msg))

    def test_extract_root_from_request(self):
        request = REQUEST_TEMPLATE.format(method='GET', route='/')
        expected = ''
        self.assert_result(request, expected)

    def test_extract_simple_path_from_request(self):
        request = REQUEST_TEMPLATE.format(method='GET', route='/some-path')
        expected = 'some-path'
        self.assert_result(request, expected)

    def test_extract_compose_path_from_request(self):
        request = REQUEST_TEMPLATE.format(
            method='GET', route='/some-path/other-path')
        expected = 'some-path/other-path'
        self.assert_result(request, expected)

    def test_extract_filename_path_from_request(self):
        request = REQUEST_TEMPLATE.format(method='GET', route='/css/style.css')
        expected = 'css/style.css'
        self.assert_result(request, expected)

    def test_extract_filename_path_from_post_request(self):
        request = REQUEST_TEMPLATE.format(method='POST', route='/')
        expected = ''
        self.assert_result(request, expected)

    def test_extract_filename_path_from_delete_request(self):
        request = REQUEST_TEMPLATE.format(method='DELETE', route='/')
        expected = ''
        self.assert_result(request, expected)


@target_function('read_file')
class ReadFileTestCase(unittest.TestCase):
    def assert_read(self, filename, read_data):
        fullpath = Path() / 'subdir' / filename
        m = mock_open(read_data=read_data)
        with patch('utils.open', m):
            received = utils.read_file(fullpath)

        self.assertEqual(read_data, received, msg=error_message(
            f'Algo deu errado! O conteúdo do arquivo "{fullpath}" deveria ser "{read_data}", mas foi "{received}"'))

    def test_read_txt_file(self):
        filename = Path() / 'subdir' / 'textfile.txt'
        self.assert_read(filename, 'Some text')

    def test_read_html_file(self):
        filename = Path() / 'subdir' / 'textfile.html'
        self.assert_read(filename, '<html></html>')

    def test_read_css_file(self):
        filename = Path() / 'subdir' / 'textfile.css'
        self.assert_read(filename, 'p {color: "red"}')

    def test_read_js_file(self):
        filename = Path() / 'subdir' / 'textfile.js'
        self.assert_read(filename, 'console.log("OK");')

    def test_read_jpg_file(self):
        filename = Path() / 'subdir' / 'textfile.jpg'
        self.assert_read(filename, bytes(
            [1, 3, 2, 5, 234, 23, 123, 23, 2, 255]))

    def test_read_png_file(self):
        filename = Path() / 'subdir' / 'textfile.png'
        self.assert_read(filename, bytes(
            [1, 3, 2, 5, 234, 23, 123, 23, 2, 255]))


@target_function('load_data')
class LoadDataTestCase(unittest.TestCase):
    def test_load_data_from_file(self):
        expected = [
            {
                "titulo": "Receita de miojo",
                "detalhes": "Bata com um martelo antes de abrir o pacote. Misture o tempero, coloque em uma vasilha e aproveite seu snack :)"
            },
            {
                "titulo": "Pão doce",
                "detalhes": "Abra o pão e coloque o seu suco em pó favorito."
            },
        ]
        m = mock_open(read_data=json.dumps(expected))
        with patch('utils.open', m):
            received = utils.load_data('data.json')

        self.assertIsInstance(received, list, msg=error_message(
            f'Algo deu errado! O retorno deveria ser uma lista, mas foi do tipo {type(received).__name__}. Obtido: {received}'))
        self.assertEqual(expected, received, msg=error_message(
            f'Algo deu errado! O conteúdo do arquivo "data.json" deveria ser "{expected}", mas foi "{received}"'))
        self.assertEqual(Path(m.call_args[0][0]), Path('data/data.json'), msg=error_message(
            f'Algo deu errado! O arquivo aberto deveria ser "data/data.json", mas foi "{Path(m.call_args[0][0])}"'))


@target_function('load_template')
class LoadTemplateTestCase(unittest.TestCase):
    def assert_template_loaded(self, filename, expected):
        m = mock_open(read_data=expected)
        with patch('utils.open', m):
            received = utils.load_template(filename)
        self.assertEqual(expected, received, msg=error_message(
            f'Algo deu errado! O conteúdo do arquivo "{filename}" deveria ser "{expected}", mas foi "{received}"'))
        self.assertEqual(Path(m.call_args[0][0]), Path('templates') / filename, msg=error_message(
            f'Algo deu errado! O arquivo aberto deveria ser "templates/{filename}", mas foi "{Path(m.call_args[0][0])}"'))

    def test_load_template_from_file(self):
        expected = '<h1>{title}</h1>'
        self.assert_template_loaded('template.html', expected)

    def test_load_component_template(self):
        expected = '<p>{text}</p>'
        self.assert_template_loaded('components/component.html', expected)





@target_function('build_response')
class BuildResponseTestCase(unittest.TestCase):
    def test_build_empty_response(self):
        function_call = 'build_response()'
        expected = 'HTTP/1.1 200 OK\n\n'.encode()
        msg = f'Algo deu errado! Para a chamada de função {function_call}, era esperado que o retorno fosse {expected}\n'

        try:
            response = utils.build_response()
        except Exception as e:
            msg += 'Para o cenário indicado acima, a solução gera o seguinte erro:\n'
            msg += f'\n{type(e).__name__}: {e}'
            self.assertTrue(False, msg=error_message(msg))

        self.assertIsInstance(response, bytes, msg=error_message(
            f'{msg}\nO retorno da função deveria estar em bytes (uso do método encode()), porém o retorno obtido foi do tipo {type(response).__name__}. Obtido: {response}'))

        msg += f'Obtido: {response}'
        self.assertEqual(expected, response, msg=error_message(msg))

    def test_build_response_with_body(self):
        function_call = 'build_response("body of the response")'
        expected = 'HTTP/1.1 200 OK\n\nbody of the response'.encode()
        msg = f'Algo deu errado! Para a chamada de função {function_call}, era esperado que o retorno fosse {expected}\n'

        try:
            response = utils.build_response('body of the response')
        except Exception as e:
            msg += 'Para o cenário indicado acima, a solução gera o seguinte erro:\n'
            msg += f'\n{type(e).__name__}: {e}'
            self.assertTrue(False, msg=error_message(msg))

        self.assertIsInstance(response, bytes, msg=error_message(
            f'{msg}\nO retorno da função deveria estar em bytes (uso do método encode()), porém o retorno obtido foi do tipo {type(response).__name__}. Obtido: {response}'))

        msg += f'Obtido: {response}'
        self.assertEqual(expected, response, msg=error_message(msg))

    def test_build_response_with_body_kwarg(self):
        function_call = 'build_response(body="body of the response")'
        expected = 'HTTP/1.1 200 OK\n\nbody of the response'.encode()

        msg = f'Algo deu errado! Para a chamada de função {function_call}, era esperado que o retorno fosse {expected}\n'

        try:
            response = utils.build_response(body='body of the response')
        except Exception as e:
            msg += 'Para o cenário indicado acima, a solução gera o seguinte erro:\n'
            msg += f'\n{type(e).__name__}: {e}'
            self.assertTrue(False, msg=error_message(msg))

        self.assertIsInstance(response, bytes, msg=error_message(
            f'{msg}\nO retorno da função deveria estar em bytes (uso do método encode()), porém o retorno obtido foi do tipo {type(response).__name__}. Obtido: {response}'))

        msg += f'Obtido: {response}'
        self.assertEqual(expected, response, msg=error_message(msg))

    def test_build_response_with_code(self):
        function_call = 'build_response(code=404, reason="Not Found")'
        expected = 'HTTP/1.1 404 Not Found\n\n'.encode()

        msg = f'Algo deu errado! Para a chamada de função {function_call}, era esperado que o retorno fosse {expected}\n'

        try:
            response = utils.build_response(code=404, reason='Not Found')
        except Exception as e:
            msg += 'Para o cenário indicado acima, a solução gera o seguinte erro:\n'
            msg += f'\n{type(e).__name__}: {e}'
            self.assertTrue(False, msg=error_message(msg))

        self.assertIsInstance(response, bytes, msg=error_message(
            f'{msg}\nO retorno da função deveria estar em bytes (uso do método encode()), porém o retorno obtido foi do tipo {type(response).__name__}. Obtido: {response}'))

        msg += f'Obtido: {response}'
        self.assertEqual(expected, response, msg=error_message(msg))

    def test_build_response_with_code_and_header(self):
        function_call = 'build_response(code=302, reason="See Other", headers="Location /")'
        expected = 'HTTP/1.1 302 See Other\nLocation /\n\n'.encode()

        msg = f'Algo deu errado! Para a chamada de função {function_call}, era esperado que o retorno fosse {expected}\n'

        try:
            response = utils.build_response(
                code=302, reason='See Other', headers='Location /')
        except Exception as e:
            msg += 'Para o cenário indicado acima, a solução gera o seguinte erro:\n'
            msg += f'\n{type(e).__name__}: {e}'
            self.assertTrue(False, msg=error_message(msg))

        self.assertIsInstance(response, bytes, msg=error_message(
            f'{msg}\nO retorno da função deveria ser em bytes (uso do método encode()), porém o retorno obtido foi do tipo {type(response).__name__}. Obtido: {response}'))

        msg += f'Obtido: {response}'
        self.assertEqual(expected, response, msg=error_message(msg))


if __name__ == '__main__':
    unittest.main()
