from database import models
from crypt.data_crypt import ByPeewee


if __name__ == '__main__':
    # Para inserir dados criptografados, seguir o exemplo:
    user = ByPeewee(models.Usuario)

    # Create ----------

    # user_name = input('Por favor insira o nome do usuário: \n')
    # user_email = input('Por favor insira o email do usuário: \n')
    # user_password = input('Por favor insira a senha de acesso: \n')
    # user_nascimento = input('Por favor insira a data de nascimento no formato dd-mm-aaaa: \n')
    # user_cep = input('Por favor insira o cep do usuário: \n')

    # user.create(
    #     data={'cep': user_cep, 'data_nascimento': user_nascimento, 'password': user_password},
    #     data_cripty={'nome': user_name, 'email': user_email}
    # )

    # Get ----------
    instance_id = int(input('ID do usuário que deseja pegar os dados: \n'))
    print(user.get_decrypt(instance_id))
