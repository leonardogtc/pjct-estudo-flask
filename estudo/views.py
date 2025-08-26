from estudo import app
from flask import render_template, url_for, request

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


@app.route('/contato')
def novapage():
    context = {}
    
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
        context.update({'pesquisa': pesquisa})
        print(pesquisa)

    return render_template('contato.html', context=context)


if __name__ == '__main__':
    app.run(debug=True)

#
