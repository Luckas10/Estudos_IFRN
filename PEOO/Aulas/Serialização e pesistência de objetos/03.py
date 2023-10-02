import pickle

lista1 = ["Chico", "123", "4.5"]

arq = open("teste.bin", "wb")

pickle.dump(lista1, arq)

arq.close()