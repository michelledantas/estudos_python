#gerar uma lista de 10 elementos randomicos e depois informar:
#-maior valor
#-menor valor
#-media dos valores
#-soma dos valores
#-criar lista de pares e de impares
from random import randint

lista = []
pares = []
impares = []
for i in range (10):
    nroGerado = randint(0,99)
    lista.append(nroGerado)
print(lista)

maior = -1
menor = 100
soma = 0

for elemento in lista: #para cada elemento da lista:
    if elemento > maior:
        maior = elemento
    if elemento < menor:
        menor = elemento
    soma = soma + elemento

    if elemento%2 == 0 : #significa que o nro é par
        pares.append(elemento)
    else:
        impares.append(elemento)

print("maior elemento: " + str(maior))
print('menor elemento: ' + str(menor))
print('soma: ' + str(soma))
media = soma/10
print('media: ' + str(media))
print('pares: ')
print(pares)
print('impares: ')
print(impares)
