from flask import Flask

app = Flask(__name__)

# Para importar a página homepage do arquivo view.py do pacote estudo.
from estudo.views import homepage
