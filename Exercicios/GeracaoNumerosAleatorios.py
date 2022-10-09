#Faça um programa que gere números aleatórios entre 5 e 95 até gerar um número divisível por 7.
# Quando isso ocorrer informar:
#- a quantidade de números divisíveis por 4 e maiores que 30 que foram gerados
#- a quantidade de números pares OU menores que 30 que foram gerados.
#- o percentual de números pares e o percentual de números impares
#- o percentual de números ímpares dentre os números gerados que eram menores que 60
#- o maior número par gerado
#- o menor número impar gerado

from random import randint
i=1
qtddDiv4Maior30 = 0
qtddParOuMenor30 = 0
qtddNrosPares = 0
qtddNrosImpares = 0
cont = 0
qtddNrosImparesMaior60 = 0
contMenor60 =0
imparMenor60 = 0
maiorPar = 0
menorImpar = 95
while i !=0:
    randomico = randint(5, 95)
    cont += 1
    print(randomico)
    if randomico%4==0 and randomico>30:
        qtddDiv4Maior30 +=1
    if randomico%2==0 or randomico<30:
        qtddParOuMenor30 +=1
    if randomico%2==0:
        qtddNrosPares +=1
        if randomico > maiorPar:
            maiorPar = randomico
    if randomico%2==1:
        qtddNrosImpares +=1
        if randomico < menorImpar:
            menorImpar=randomico
    if randomico < 60:
        contMenor60 +=1
        if randomico%2==1:
            imparMenor60 +=1

    if randomico%7==0:
        break
  # - o percentual de números ímpares dentre os números gerados que eram menores que 60


print("A quantidade de números divisíveis por 4 e maiores que 30 que foram gerados é: {}".format(qtddDiv4Maior30))
print("A quantidade de números pares OU menores que 30 que foram gerados é: {}".format(qtddParOuMenor30))

if qtddNrosPares > 0:
    percentualPares = (qtddNrosPares/cont)*100
    print("O percentual de números pares é: {}% ".format(percentualPares))
else:
    print("O percentual de números pares é 0%")

if qtddNrosImpares > 0:
    percentualImpares = (qtddNrosImpares/cont)*100
    print("O percentual de números impares é: {}% ".format(percentualImpares))
else:
    print("O percentual de números impares é 0%")

if imparMenor60 >0:
    percentualImparMenor60 = (imparMenor60 / contMenor60) * 100
    print("O percentual de números impares menores que 60 é: {}% ".format(percentualImparMenor60))
else:
    print("O percentual de números impares menores que 60 é: 0%")

print("O maior número par gerado é: {}".format(maiorPar))
print("O menor número impar gerado é: {}".format(menorImpar))
print("Contador: "+ str(cont))