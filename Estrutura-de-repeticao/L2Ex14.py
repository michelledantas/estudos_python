# Faça um programa que gere números aleatórios entre 0 e 50 até o número 32 ser
# gerado. Quando isso ocorrer, informar:
# a. A soma de todos os números gerados
# b. A quantidade de números gerados que é impar
# c. O menor número gerado

from random import randint

nro = 0
cont = 0
soma = 0
qtddImpares = 0
#defini menor como 50 pois quando deixo como 0 não funciona corretamente
menor = 50
while nro !=32:
    nro = randint(0, 50)
    if nro % 2 != 0:
        qtddImpares = qtddImpares + 1
    cont = cont + 1
    soma = soma + nro
    print(nro)
    if nro < menor:
        menor = nro

print('A soma de todos os números gerados é: ' + str(soma))
print('A quantidade de impares: ' + str(qtddImpares))
print('O menor número gerado é: ' + str(menor))