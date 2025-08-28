from estudo import app, db
from estudo.models import Contato
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


@app.route('/contato', methods=['GET', 'POST'])
def novapage():
    context = {}

    # if request.method == 'GET':
    #     pesquisa = request.args.get('pesquisa')
    #     context.update({'pesquisa': pesquisa})
    #     print(pesquisa)

    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']

        contato = Contato(nome=nome, email=email,
                          assunto=assunto, mensagem=mensagem)
        db.session.add(contato)
        db.session.commit()

    return render_template('contato.html', context=context)


if __name__ == '__main__':
    app.run(debug=True)

#
