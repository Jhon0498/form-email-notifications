from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)

# Essa chave é usada para proteger informações como session e formulários
app.config['SECRET_KEY'] = 'minha-chave-secreta'

#inicia o bootstrap
bootstrap = Bootstrap(app)

# inicia o Flask-Moment
moment = Moment(app)

# Envia o aplicativo para routes.py
# para que as rotas sejam criadas
from routes import registrar_rotas
registrar_rotas(app)

if __name__ == '__main__':
    app.run(debug=True)