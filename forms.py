from flask_wtf import FlaskForm

# importa os campos que será utilizado
from wtforms import StringField, SubmitField, SelectField, PasswordField

# importa os validadores
from wtforms.validators import DataRequired


class FormularioAluno(FlaskForm):

    # Campo para informar o usuário cadastrado
    usuario = StringField(
        'What is your name?',
        validators=[DataRequired()]
    )

    # botão que envia o formulário
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
            'placeholder': 'Informe a sua senha'
        }
    )

    submit = SubmitField('Enviar')