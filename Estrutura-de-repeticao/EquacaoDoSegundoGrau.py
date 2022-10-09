# Faça um programa que resolva a equação do segundo grau em python, verificando:
#  - se existem duas raízes reais
#  - se existe uma raiz real
#  - não existe solução nos números reais

import math

print("Vamos calcular uma equação do Segundo Grau.\nVou precisar que você me informe os valores de a, b e c.\nAtenção a precisa ser diferente de 0")
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if a == 0:
    print("O valor do coeficiente a nunca é igual a 0, nesse caso, a equação deixa de ser do 2º grau.")

else:
    print("Primeiro passo, vamos calcular o Δ. \nΔ = b² - ac")
    #delta = b² - 4ac
    delta = (b ** 2) - 4 * a * c
    print("Δ= " + str(delta))

    # → discriminante positivo(Δ > 0): duas soluções para a equação;
    #Ex a=1; b=–1 c=–12
    if delta > 0:
        print("Quando Δ > 0, ou seja, positivo existe duas soluções para a equação: x1 e x2")
        print("Agora vamos calcular a fórmula de Baskara \nx = (-b +- √Δ)/2a ")
        raizDelta = math.sqrt(delta)
        print("A raiz de delta é: " + str(raizDelta))
        x1 = (-b + raizDelta)/2*a
        x2 = (-b - raizDelta)/2*a
        print("O valor de x1 = " + str(x1) + "\nO valor de x2 = " + str(x2))

    # → discriminante igual a zero(Δ=0): as soluções da equação são repetidas;
    #Ex a=4 b=-4 c=1
    elif delta == 0:
          print("Quando Δ = 0 as soluções são repetidas")
          print("Agora vamos calcular a fórmula de Baskara \nx= (-b +- √Δ)/2a ")
          raizDelta = math.sqrt(delta)
          print("A raiz de delta é: " + str(raizDelta))
          x1 = (-b + raizDelta) / 2 * a
          x2 = (-b - raizDelta) / 2 * a
          print("O valor de x1 = " + str(x1) + "\nO valor de x2 = " + str(x2))

    # → discriminante  negativo(Δ < 0): não admite solução real.
    #Ex a=1 b=-4 c=5
    else:
        print("Quando o valor de Δ for negativo, não adminite solução real. ")


