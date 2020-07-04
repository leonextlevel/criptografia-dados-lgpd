import datetime
from database import models
from reportlab.pdfgen import canvas
from database.connection import db
from utils.transform import normalize_key


class GeneratePDF:

    def __init__(self, filename):
        self.filename = filename
        self.pdf = canvas.Canvas('{}.pdf'.format(filename))

    @staticmethod
    def get_noticias(instance_id):
        cursor = db.execute_sql(f'SELECT * FROM perfilusuarionoticia WHERE usuario_id = {instance_id};')
        noticias = []
        for row in cursor:
            noticia = row[2]
            noticias.append(models.Noticia.get_by_id(noticia).titulo)
        print(noticias)
        return noticias

    
    def generate(self, data):
        self.pdf = canvas.Canvas('{}.pdf'.format(data['id']))
        self.pdf.setFont('Helvetica-Bold', 14)
        self.pdf.drawString(160, 750, 'Relatório de dados do usuário')
        self.pdf.setFont('Helvetica-Bold', 12)
        self.pdf.drawString(70, 720, '1 - Dados pessoais do usuário, perfil completo contendo.')
        y = 700
        for k, v in data.items():
            if k == 'password':
                continue
            info = '%s: %s' % (normalize_key(k), v)
            self.pdf.drawString(100, y, info)
            y -= 15
        self.pdf.drawString(70, 600, '2 - Dados encontrados no banco relacionados ao ID do usuário:')
        x = 100
        y = 585
        noticias = GeneratePDF.get_noticias(data['id'])
        if len(noticias) != 0:
            for noticia in noticias:
                self.pdf.drawString(x, y, 'O usuário ' + str(data['nome']) + ' acessou a notícia ' + noticia + '.')
                y = y - 15
        else:
            self.pdf.drawString(x, y, 'Não foram encontrados registros relacionados a este usuário.')
            self.pdf.save()


if __name__ == '__main__':
    informacoes_pessoais = {
        'id': 28,
        'nome': 'jonas',
        'cep': '12999000',
        'data_nascimento': datetime.date(2000, 1, 1),
        'email': 'jonas@email.com',
        'password': 'nsbcdhh'
    }
    informacoes_de_uso = {
        'perfilusuarionoticia': [1, 2, 3],
        'snknsakd': []
    }
    informacoes_da_noticia = {
        '1': {
            'titulo': 'aaaa',
            'tema': 'esporte'
        },
        '2': {
            'titulo': 'bbbbb',
            'tema': 'esporte'
        },
        '3': {
            'titulo': 'cccc',
            'tema': 'esporte'
        },
    }
    g = GeneratePDF('teste')
    g.generate(informacoes_pessoais)
