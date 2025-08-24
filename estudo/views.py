from estudo import app
from flask import render_template

# Para importar a página homepage do arquivo view.py do pacote estudo.


@app.route('/')
def homepage():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

#
