from flask_wtf import FlaskForm
#importa os campos que será utilizado
from wtforms import StringField, SubmitField, SelectField, PasswordField
#importa os validadores
from wtforms.validators import DataRequired


class FormularioAluno(FlaskForm):

    #StringField é uma "caixa"para digitar o texto (nome)
    nome = StringField(
        'Informe o seu nome:',
        validators=[DataRequired()] #informa que o campo não pode ficar vazio
    )

    sobrenome = StringField(
        'Informe o seu sobrenome:',
        validators=[DataRequired()]
    )

    instituicao = StringField(
        'Informe a intituição de ensino:',
        validators=[DataRequired()]
    )

    disciplina = SelectField(
        'Informe a disciplina:', #Lista
        choices=[
            ('DSWA5', 'DSWA5'),
            ('DSWA6', 'DSWA6'),
            ('DSWA7', 'DSWA7')
        ]
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