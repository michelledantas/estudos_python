#2 – Gere uma lista de 30 números aleatórios entre 1 e 100.
# Não pode haver número repetido na lista.
from random import randint

lista = []

#for i in range(30): antes era com o for
cont = 0
while cont < 30:
    nro = randint(1,100)
    existe = False # vou assumir que o número ainda nao está na lista
    #percorrer toda a lista e ver se o nro gerado está ou nao nela
    for elemento in lista: # para cada elemento da lista:
        if nro == elemento:
            existe = True
    #if existe == False: #significa que percorri toda a lista e nao achei 'nro' nela
    if not existe :
        lista.append(nro)
        cont = cont + 1

print(lista)
