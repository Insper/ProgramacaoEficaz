from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    print(request.method)
    print(request.headers)

    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)
