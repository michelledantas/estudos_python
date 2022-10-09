# Faça um programa para o usuário adivinhar o número sorteado:
# O programa deve perguntar o valor limite para o sorteio (ex: se o usuário informar o número 10,
# o programa irá sortear um número entre 0 e 10, inclusive o 10).
# O programa deve sortear o número e pedir ao usuário que tente adivinhar o número.
# Caso o usuário não acerte o palpite o programa deve dizer se o número sorteado é maior ou menor que o informado pelo usuário.
# O programa deve continuar pedindo palpites até que o usuário acerte.
# No final o programa deve informar quantos palpites foram necessários até que o palpite fosse o correto

from random import randint

limite = int(input("Digite um número para ser o valor limite do sorteio: "))
x= 0
cont = 0
randomico = randint(0,limite)
palpite = int(input("Qual o seu palpite sobre o número sorteado: "))
while x == 0:
    cont += 1
    if randomico == palpite:
        print("Você acertou o número sorteado.")
        break
    elif randomico > palpite:
        print("O número sorteado é maior que o seu palpite.")
        palpite = int(input("Digite novamente o seu palpite: "))
    else:
        print("O número sorteado é menor que o seu palpite.")
        palpite = int(input("Digite novamente o seu palpite: "))
print("Foram necessários {} palpites para acertar o número sorteado.".format(cont))