import datetime

from reportlab.pdfgen import canvas

from utils.transform import normalize_key


class GeneratePDF:

    def __init__(self, filename):
        self.filename = filename
        self.pdf = canvas.Canvas('{}.pdf'.format(filename))
    
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
