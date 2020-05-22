from cryptography.fernet import Fernet

'''
Classe responsável pela criação da chave de criptografia
'''
class InsertByPeewee:

    def __init__(self, model_class, **kwargs):
        self.model_class = model_class

    @staticmethod
    def generate_key():    
        # Método responsável por gerar a chave de criptografia 
        # aleatória usando a biblioteca criptography
        return Fernet.generate_key()

    @staticmethod
    def save_key(key):
        file = open("./keys.key", "w+")
        file.write(str(key))
        file.close()
        return

    
    def create(self, data, data_cripty):
        chave = self.generate_key()
        f = Fernet(chave)
        self.save_key(chave)
        for k, v in data_cripty.items():
            v_encrypt = f.encrypt(str.encode(v))
            data.update({k: v_encrypt})
        instance = self.model_class.create(**data)
        return instance

        




        



