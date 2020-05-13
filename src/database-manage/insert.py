from models import Usuario, Noticia, Tema, PerfilUsuarioNoticia
from cryptography.fernet import Fernet
from ..crypt.generate_data_crypt import InsertByPeewee


if __name__ == '__main__':
    # Para inserir dados criptografados, seguir o exemplo:
    user = InsertByPeewee(Usuario)
    user.create(data={'cep': '33333-333', 'data_nascimento': '02-01-2000', 'password': '12345'}, data_cripty={'nome': 'Teste', 'email': 'teste@email.com'})
    # user.create(nome='Clayton', cep='22222-222', data_nascimento='01-01-2000', email='clay@email.com', password='123456')


# tema1, _ = Tema.get_or_create(nome='Tecnologia')
# tema2, _ = Tema.get_or_create(nome='Saúde')
# tema3, _ = Tema.get_or_create(nome='Negócios')
# tema4, _ = Tema.get_or_create(nome='Mundial')

# usuario1, _ = Usuario.get_or_create(
#     nome='Juscelino Lopes',
#     cep='40028-922',
#     data_nascimento='15-11-2000',
#     email='juscelino@email.com',
#     password='senhadificil'
# )

# usuario2, _ = Usuario.get_or_create(
#     nome='Matheus Otavio Silveira',
#     cep='12345-000',
#     data_nascimento='12-12-1999',
#     email='math@email.com',
#     password='ojogo123'
# )

# noticia1, _ = Noticia.get_or_create(
#     titulo="CoronaVirus mata milhões",
#     data_hora="10-03-2020 12:00:00",
#     conteudo="Corona chega matando tudo que vê pela frente.",
#     cep="45454-545",
#     tema=tema2
# )

# noticia2, _ = Noticia.get_or_create(
#     titulo="Jovem listado como melhor jogador de LoL do mundo",
#     data_hora="16-07-2019 13:34:00",
#     conteudo="Matheus Rothstein, após ganhar o campeonato mundial de League of Legends é declarado como melhor jogador mundial de LoL, com votação praticamente unânime.",
#     cep="2223-535",
#     tema=tema1
# )

# noticia3, _ = Noticia.get_or_create(
#     titulo="Dolar ultrapassa a marca de 5 reais",
#     data_hora="17-03-2020 23:47:00",
#     conteudo="O valor comercial do dolar chega a R$ 5,01, durante a terça feira, 17 de fevereiro",
#     cep="2133-533",
#     tema=tema3
# )

# noticia4, _ = Noticia.get_or_create(
#     titulo="Estudante é a nova vítima do Corona Vírus",
#     data_hora="14-03-2020 18:50:00",
#     conteudo="Estudante da Fatec passa férias no Japão e volta infectado, ele se encontra isolado na sala da coordenação.",
#     cep="12230-676",
#     tema=tema2
# )

# noticia5, _ = Noticia.get_or_create(
#     titulo="Com crise Xiaomi bota Apple para mamar",
#     data_hora="17-01-2020 23:47:00",
#     conteudo="Com crise mundial Xiaomi, produz robôs para fazerem celulares aumentando a renda chinesa",
#     cep="21330-533",
#     tema=tema3
# )

# noticia6, _ = Noticia.get_or_create(
#     titulo="Alunos que trabalham na NASA, estudaram na Fatec",
#     data_hora="19-08-2019 19:50:00",
#     conteudo="Alunos do curso de análise e desenvolvimento de sistemas, da Fatec de São José dos Campos, se destacam no mercado internacional.",
#     cep="12390-676",
#     tema=tema4
# )

# noticia7, _ = Noticia.get_or_create(
#     titulo ="Playstation 5 no Brasil",
#     data_hora="01-03-2020 17:47:00",
#     conteudo="Preço do PlayStation 5 passa de 5 mil reais, devido altos impostos",
#     cep="12310-500",
#     tema=tema1
# )

# noticia8, _ = Noticia.get_or_create(
#     titulo="Palmeiras continua sem Mundial",
#     data_hora="14-03-2020 23:47:00",
#     conteudo="Nada muda, o palmeiras continua sem mundial",
#     cep="12310-500",
#     tema=tema4
# )

# p1, _ = PerfilUsuarioNoticia.get_or_create(
#     usuario=usuario1,
#     noticia=noticia1
# )

# p2, _ = PerfilUsuarioNoticia.get_or_create(
#     usuario=usuario1,
#     noticia=noticia3
# )

# p3, _ = PerfilUsuarioNoticia.get_or_create(
#     usuario=usuario1,
#     noticia=noticia4
# )

# p4, _ = PerfilUsuarioNoticia.get_or_create(
#     usuario=usuario1,
#     noticia=noticia8
# )

# p5, _ = PerfilUsuarioNoticia.get_or_create(
#     usuario=usuario2,
#     noticia=noticia6
# )

# p6, _ = PerfilUsuarioNoticia.get_or_create(
#     usuario=usuario2,
#     noticia=noticia1
# )

# p6, _ = PerfilUsuarioNoticia.get_or_create(
#     usuario=usuario2,
#     noticia=noticia2
# )


