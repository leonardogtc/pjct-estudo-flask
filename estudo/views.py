from estudo import app
from flask import render_template, url_for

# Para importar a página homepage do arquivo view.py do pacote estudo.


@app.route('/')
def homepage():
    usuario = 'Leonardo'
    idade = 54

    context = {
        'usuario': usuario,
        'idade': idade
    }
    return render_template('index.html', context=context)


@app.route('/sobre')
def novapage():
    return "nova página"


if __name__ == '__main__':
    app.run(debug=True)

#
