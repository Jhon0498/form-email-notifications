from flask import render_template
from datetime import datetime

from forms import FormularioAluno

from flask_mail import Message


def registrar_rotas(app, mail):

    # Usuários cadastrados temporariamente
    usuarios = {
        'jhonatan': {
            'prontuario': 'PT3026931',
            'nome': 'Jhonatan Mendes Morão'
        }
    }

    @app.route('/', methods=['GET', 'POST'])
    def index():

        # Cria o formulário
        form = FormularioAluno()

        # Se o usuário clicou em Submit
        # E o campo foi preenchido corretamente
        if form.validate_on_submit():

            # Pega o usuário informado no formulário
            usuario = form.usuario.data

            # Procura o usuário cadastrado
            dados_usuario = usuarios.get(usuario)

            # Verifica se o usuário existe
            if dados_usuario:

                # Pega o prontuário do usuário cadastrado
                prontuario = dados_usuario['prontuario']

                # Pega o nome do usuário cadastrado
                nome = dados_usuario['nome']

                # Pega os e-mails cadastrados nas variáveis de ambiente
                destinatarios = app.config['FLASKY_ADMIN'].split(',')

                # Cria o e-mail que será enviado
                mensagem = Message(
                    subject='Novo cadastro realizado',
                    recipients=destinatarios
                )

                # Monta o conteúdo do e-mail
                mensagem.body = f'''Prontuário: {prontuario}
Nome: {nome}
Usuário: {usuario}
'''

                # Envia o e-mail através do Mailgun
                mail.send(mensagem)

                # Mostra a página novamente
                # depois que o e-mail foi enviado
                return render_template(
                    'index.html',
                    form=form,
                    nome=nome,
                    current_time=datetime.utcnow()
                )

        # Quando a pessoa entra pela primeira vez,
        # ainda não existe nenhum dado preenchido
        return render_template(
            'index.html',
            form=form,
            current_time=datetime.utcnow()
        )