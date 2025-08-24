from estudo import app
from flask import render_template, url_for

# Para importar a página homepage do arquivo view.py do pacote estudo.


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/sobre')
def novapage():
    return "nova página"


if __name__ == '__main__':
    app.run(debug=True)

#
