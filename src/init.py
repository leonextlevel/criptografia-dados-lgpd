from database import models


if __name__ == '__main__':
    try:
        models.Usuario.create_table()
        print("Tabela 'Usuario' criada com sucesso!")
    except peewee.OperationalError as e:
        print("Tabela 'Usuario' ja existe!")
        print(e)

    try:
        models.Tema.create_table()
        print("Tabela 'Tema' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Tema' ja existe!")

    try:
        models.Noticia.create_table()
        print("Tabela 'Noticia' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Noticia' ja existe!")

    try:
        models.PerfilUsuarioNoticia.create_table()
        print("Tabela 'PerfilUsuarioNoticia' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'PerfilUsuarioNoticia' ja existe!")