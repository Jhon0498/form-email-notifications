from flask_wtf import FlaskForm
#importa os campos que será utilizado
from wtforms import StringField, SubmitField, SelectField, PasswordField
#importa os validadores
from wtforms.validators import DataRequired


class FormularioAluno(FlaskForm):

    #StringField é uma "caixa"para digitar o texto (nome)
    nome = StringField(
        'What is your name:',
        validators=[DataRequired()] #informa que o campo não pode ficar vazio
    )

    #botão que envia o formulário
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    usuario = StringField(
        validators=[DataRequired()],
        render_kw={
            'placeholder': 'Usuário ou e-mail'
    }
 )
    senha = PasswordField(
        'Informe a sua senha',
        validators=[DataRequired()],
        render_kw={
        'placeholder': 'Informe a sua senha',
    }
 )

    submit = SubmitField('Enviar')