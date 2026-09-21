import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from dotenv import load_dotenv


# Carrega as variáveis do arquivo .env
load_dotenv()


app = Flask(__name__)

# Chave para proteger sessões e formulários
app.config['SECRET_KEY'] = 'minha-chave-secreta'


# Configurações do Mailgun
app.config['MAILGUN_API_KEY'] = os.environ.get('MAILGUN_API_KEY')
app.config['MAILGUN_DOMAIN'] = os.environ.get('MAILGUN_DOMAIN')
app.config['MAILGUN_BASE_URL'] = os.environ.get(
    'MAILGUN_BASE_URL',
    'https://api.mailgun.net'
)

# E-mail que receberá as mensagens
app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')


# Inicializa Bootstrap
bootstrap = Bootstrap(app)


# Inicializa Flask-Moment
moment = Moment(app)


# Registra as rotas
from routes import registrar_rotas
registrar_rotas(app)


if __name__ == '__main__':
    app.run(debug=True)