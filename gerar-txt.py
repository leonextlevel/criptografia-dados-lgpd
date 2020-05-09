arquivo = open("arquivo.txt", "w")

arquivo.write("Essa é a primeira linha. \n")
arquivo.write("Essa é a nossa segunda linha. \n")

with open("arquivo.txt","r+") as arquivo:

    arquivo.write("Estou escrevendo")

    arquivo.readline()

arquivo.close()
