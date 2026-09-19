import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_mail import Mail


app = Flask(__name__)

# Chave para proteger sessões e formulários
app.config['SECRET_KEY'] = 'minha-chave-secreta'

# Configuração do e-mail - Zoho
app.config['MAIL_SERVER'] = 'smtp.zoho.com'
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

# ...
# Incluir o trecho para resgatar o e-mail do Admin das variáveis de ambiente
app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')
# ...

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            if app.config['FLASKY_ADMIN']:
                send_email(app.config['FLASKY_ADMIN'], 'New User',
                           'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False))

# Registra as rotas
from routes import registrar_rotas
registrar_rotas(app)

if __name__ == '__main__':
    app.run(debug=True)
