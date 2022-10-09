#Gere uma lista de 30 números aleatórios entre 1 e 100. 
#Não pode haver número repetido na lista.

from random import randint
lista = []

for i in range(30):
    nro = randint(1,100)
    if nro not in lista:
        lista.append(nro)
    else:
        print("O número {} foi gerado repetido.".format(nro))
lista.sort()
print(lista)