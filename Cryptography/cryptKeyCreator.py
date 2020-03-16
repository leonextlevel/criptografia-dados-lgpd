from cryptography.fernet import Fernet

'''
Classe responsável pela criação da chave de criptografia
'''
class KeyCreator:

    def __init__(self):
    # Construtor da classe 
        self.writeKeyAndCloseFile()
    
    def generate_key(self):    
    # Método responsável por gerar a chave de criptografia 
    # aleatória usando a biblioteca criptography

        self.key = Fernet.generate_key()
        return self.key

    def createFile(self):
    # Método responsável por criar um arquivo com a extensão .key para que esteja armazenado a 
    # chave de criptografia gerada

        self.file = open("./cryptographyKey.key", "w+")
        return self.file
    
    def writeKeyAndCloseFile(self):
    # Método responsável por instânciar uma chave e um arquivo
    # salvar a chave como uma string dentro do arquivo
    # fechar o arquivo
        file = self.createFile()
        key = self.generate_key()
        file.write(str(key))
        file.close()


KeyCreator()
        




        



