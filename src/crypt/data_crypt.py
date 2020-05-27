from cryptography.fernet import Fernet, InvalidToken
from playhouse.shortcuts import model_to_dict
from vault.commands import Commands


class ByPeewee:
    '''
    Classe responsável pela criação da chave de criptografia
    '''
    commands = Commands()

    def __init__(self, model_class, **kwargs):
        self.model_class = model_class

    @staticmethod
    def generate_key():    
        # Método responsável por gerar a chave de criptografia 
        # aleatória usando a biblioteca criptography
        return Fernet.generate_key()

    def save_key(self, pk, key):
        self.commands.unseal()
        self.commands.create_secret(pk=pk, key=key)
        self.commands.seal()
    
    def create(self, data, data_cripty):
        chave = self.generate_key()
        f = Fernet(chave)
        for k, v in data_cripty.items():
            v_encrypt = f.encrypt(str.encode(v))
            data.update({k: v_encrypt})
        instance = self.model_class.create(**data)
        self.save_key(instance._pk, str(chave))
        print('Usuário "%d" criado' % instance.id)
        return instance
    
    def get_decrypt(self, pk):
        chave = self.commands.get_secret(pk)
        instance = self.model_class.get_by_id(pk)
        data_dict = model_to_dict(instance)
        f = Fernet(str.encode(chave[2:-1]))
        new_data_dict = {}
        for k, v in data_dict.items():
            try:
                new_v = f.decrypt(str(v).encode()).decode()
                new_data_dict.update({ k: new_v })
            except InvalidToken:
                new_data_dict.update({ k: v })
        return new_data_dict
        
