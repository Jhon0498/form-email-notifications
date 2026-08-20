from flask import render_template
from datetime import datetime
from forms import FormularioAluno, LoginForm


def registrar_rotas(app):

    @app.route('/', methods=['GET', 'POST'])
    def index():

        # Cria o formulário
        form = FormularioAluno()


        # Se o usuário clicou em Submit
        # E todos os campos foram preenchidos corretamente
        if form.validate_on_submit():

            # Pega o que foi digitado no campo nome
            nome = form.nome.data

            # Pega o que foi digitado no campo sobrenome
            sobrenome = form.sobrenome.data

            # Pega a instituição digitada
            instituicao = form.instituicao.data

            # Pega a disciplina escolhida
            disciplina = form.disciplina.data


            # Mostra a página novamente,
            # mas agora levando os dados preenchidos
            return render_template(
                'index.html',

                # Envia o formulário para o HTML
                form=form,

                # Envia os dados para aparecerem no topo
                nome=nome,
                sobrenome=sobrenome,
                instituicao=instituicao,
                disciplina=disciplina,
                current_time=datetime.utcnow()
            )


        # Quando a pessoa entra pela primeira vez,
        # ainda não existe nenhum dado preenchido
        return render_template(
            'index.html',
            form=form,
            current_time=datetime.utcnow()
        )


    @app.route('/login', methods=['GET', 'POST'])
    def login():

        form = LoginForm()

        # Se o usuário clicou em enviar
        # e os campos estão preenchidos corretamente
        if form.validate_on_submit():

            # Pega o usuário ou email digitado
            usuario = form.usuario.data

            # Pega a senha digitada
            senha = form.senha.data

            return render_template(
                'login.html',
                form=form,
                usuario=usuario,
                current_time=datetime.utcnow()
            )


        # Quando o usuário entra na página
        return render_template(
            'login.html',
            form=form,
            current_time=datetime.utcnow()
        )
