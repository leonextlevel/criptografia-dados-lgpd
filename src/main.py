from database import models
from crypt.gererate_data_crypt import InsertByPeewee


if __name__ == '__main__':
    # Para inserir dados criptografados, seguir o exemplo:
    user = InsertByPeewee(models.Usuario)
    user.create(
        data={'cep': '33333-333', 'data_nascimento': '02-01-2000', 'password': '12345'},
        data_cripty={'nome': 'Teste', 'email': 'teste@email.com'}
    )
