#Escrever um programa que permita ao usuário digitar três números inteiros.
a = int(input("Digite o 1º número: "))
b = int(input("Digite o 2º número: "))
c = int(input("Digite o 3º número: "))

#Após a leitura, o programa deve verificar se os três valores podem formar um triângulo.

#if a=="0" or b="0" or c="0"
#    print("Não é possível fazer um triângulo com o número 0")
#else:

#Obs.: Para que três lados formem um triângulo,
#o comprimento de cada um dos lados tem que ser menor que a soma dos outros dois.

#| b - c | < a < b + c
#| a - c | < b < a + c
#| a - b | < c < a + b

#if a <= b + c and b <= a + c and c <= a + c:
if a < b + c or b < a + c or c < a + b:
    #Os números informados formam um triângulo
    # triângulo eqüilátero (três lados iguais)
    if a == b and a == c:
        print("Os números informados formam um triângulo equilatero, todos os lados são iguais.")
    # isósceles (dois lados iguais)
    elif a == b or a == c or c == b:
        print("Os números informados formam um triângulo isósceles com 2 lados iguais")
    # escaleno todos os lados diferentes
    elif a != b and a != c:
        print("Os números informados formam um triângulo escaleno com todos os lados diferentes")

else: print("Os números informados não formam um triângulo.")

