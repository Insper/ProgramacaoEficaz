from flask import Flask, request

app = Flask(__name__)

RESPONSE_TEMPLATE = '''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Get-it</title>
</head>
<body>

<h1>Get-it</h1>
<p>Como o Post-it, mas com outro verbo</p>

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
