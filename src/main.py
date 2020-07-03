from database import models
from crypt.data_crypt import ByPeewee
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from database.connection import db
from relatorio.gerador import GeneratePDF


def option_1():
    user_name = input('Por favor insira o nome do usuário: \n')
    user_email = input('Por favor insira o email do usuário: \n')
    user_password = input('Por favor insira a senha de acesso: \n')
    user_nascimento = input('Por favor insira a data de nascimento no formato dd-mm-aaaa: \n')
    user_cep = input('Por favor insira o cep do usuário: \n')

    user.create(
        data={'cep': user_cep, 'data_nascimento': user_nascimento, 'password': user_password},
        data_cripty={'nome': user_name, 'email': user_email}
    )


def option_2():
    instance_id = int(input('ID do usuário que deseja pegar os dados: \n'))
    print(user.get_decrypt(instance_id))
    return user.get_decrypt(instance_id)


def option_3():
    instance_id = input('ID do usuário que deseja pegar os dados: \n')
    data = user.get_decrypt(int(instance_id))
    g = GeneratePDF(instance_id)
    g.generate(data)


if __name__ == '__main__':
    # Para inserir dados criptografados, seguir o exemplo:
    user = ByPeewee(models.Usuario)

    options_dict = {
        '1': option_1,
        '2': option_2,
        '3': option_3,
    }

    option = input(
        'Por favor escolha uma opção para seguir \n'
        '1 - Criar usuário \n'
        '2 - Consultar dados cadastrais do usuário \n'
        '3 - Gerar PDF com informações do usuário\n'
    )

    options_dict[option]()