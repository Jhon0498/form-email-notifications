from flask import render_template
from datetime import datetime
from forms import FormularioAluno


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




            # Mostra a página novamente,
            # mas agora levando os dados preenchidos
            return render_template(
                'index.html',

                # Envia o formulário para o HTML
                form=form,
                # Envia os dados para aparecerem no topo
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
