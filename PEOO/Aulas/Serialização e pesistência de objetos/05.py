import pickle

# arq = open("teste.bin", "r")
arq = open("teste.bin", "rb")
arqDesserializado = pickle.load(arq)
# arqDesserializado = arq.read()

print(type(arqDesserializado))