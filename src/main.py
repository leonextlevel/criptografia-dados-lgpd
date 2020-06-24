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

def get_noticias(instance_id):
    cursor = db.execute_sql(f'SELECT * FROM perfilusuarionoticia WHERE usuario_id = {instance_id};')
    noticias = []
    for row in cursor:
        noticia = row[2]
        noticias.append(models.Noticia.get_by_id(noticia).titulo)
    print(noticias)
    return noticias


def generatePDF():
    id = getUser()
    nomeDoPDF = 'Relatório de de dados do usuário ' + id['nome']
    pdf = canvas.Canvas('{}.pdf'.format(nomeDoPDF))
    pdf.setFont('Helvetica-Bold', 14)
    pdf.drawString(160, 750, nomeDoPDF)
    pdf.setFont('Helvetica-Bold', 12)
    pdf.drawString(70, 720, '1 - Dados pessoais do usuário, perfil completo contendo.')
    pdf.drawString(100, 700, 'ID: ' + str(id['id']))
    pdf.drawString(100, 685, 'Nome: ' + str(id['nome']))
    pdf.drawString(100, 670, 'CEP: ' + str(id['cep']))
    pdf.drawString(100, 655, 'Data de nascimento: ' + str(id['data_nascimento']))
    pdf.drawString(100, 640, 'Email: ' + str(id['email']))
    pdf.drawString(100, 625, 'Password: ' + str(id['password']))
    pdf.drawString(70, 600, '2 - Dados encontrados no banco relacionados ao ID do usuário:')
    x = 100
    y = 585
    noticias = get_noticias(id['id'])
    if len(noticias) != 0:
        for noticia in noticias:
            pdf.drawString(x, y, 'O usuário ' + str(id['nome']) + ' acessou a notícia ' + noticia + '.')
            y = y - 15
    else:
        pdf.drawString(x, y, 'Não foram encontrados registros relacionados a este usuário.')
        
    
    pdf.save()


def option_3():
    instance_id = input('ID do usuário que deseja pegar os dados: \n')
    data = user.get_decrypt(int(instance_id))
    g = GeneratePDF(instance_id)
    g.generate(data)


if __name__ == '__main__':
    Para inserir dados criptografados, seguir o exemplo:
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