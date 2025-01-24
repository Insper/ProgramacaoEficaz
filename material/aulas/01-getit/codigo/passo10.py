from flask import Flask, render_template_string
import views


app = Flask(__name__)

# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'

@app.route('/')
def index():

    return render_template_string(views.index())


if __name__ == '__main__':
    app.run(debug=True)
