import peewee

from database.connection import db

'''
Modelo genérico para testes das funções que serão implementadas.

Simula um app simples de notícias.
'''


class BaseModel(peewee.Model):
    """
    Modelo base para os demais.
    """
    class Meta:
        database = db


class Usuario(BaseModel):
    nome = peewee.CharField(max_length=100)
    cep = peewee.CharField(max_length=9)
    data_nascimento = peewee.DateField(formats=['%d-%m-%Y'])
    email = peewee.CharField(max_length=150)
    password = peewee.CharField(max_length=30)


class Tema(BaseModel):
    nome = peewee.CharField(max_length=30)


class Noticia(BaseModel):
    titulo = peewee.CharField(max_length=50)
    data_hora = peewee.DateTimeField(formats=['%d-%m-%Y %H:%M:%S'])
    conteudo = peewee.TextField()
    cep = peewee.CharField(max_length=9)
    tema = peewee.ForeignKeyField(Tema)


class PerfilUsuarioNoticia(BaseModel):
    usuario = peewee.ForeignKeyField(Usuario)
    noticia = peewee.ForeignKeyField(Noticia)


if __name__ == '__main__':
    try:
        Usuario.create_table() 
        print("Tabela 'Usuario' criada com sucesso!")
    except peewee.OperationalError as e:
        print("Tabela 'Usuario' ja existe!")
        print(e)

    try:
        Tema.create_table()
        print("Tabela 'Tema' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Tema' ja existe!")

    try:
        Noticia.create_table()
        print("Tabela 'Noticia' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Noticia' ja existe!")

    try:
        PerfilUsuarioNoticia.create_table()
        print("Tabela 'PerfilUsuarioNoticia' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'PerfilUsuarioNoticia' ja existe!")