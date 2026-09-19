import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_mail import Mail

app = Flask(__name__)

# Chave para proteger sessões e formulários
app.config['SECRET_KEY'] = 'minha-chave-secreta'


# Configuração do e-mail - Mailgun
app.config['MAIL_SERVER'] = 'smtp.mailgun.org'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')


# Inicializa Flask-Mail DEPOIS da configuração
mail = Mail(app)


# Inicializa Bootstrap
bootstrap = Bootstrap(app)


# Inicializa Flask-Moment
moment = Moment(app)


# Resgata os e-mails dos destinatários
# que estão cadastrados nas variáveis de ambiente
app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')


# Registra as rotas
from routes import registrar_rotas

registrar_rotas(app, mail)


if __name__ == '__main__':
    app.run(debug=True)