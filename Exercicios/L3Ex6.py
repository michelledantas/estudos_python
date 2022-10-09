# Faça um programa que leia um número digitado pelo usuário.
# Depois, informe todos os números primos gerados até o número digitado pelo usuário.

num = int(input("Digite um número: "))
primos = ""

#loop com números até chegar ao que foi digitado pelo usuário
for a in range (1, num + 1):
    contador = 0

    #loop para testar se o resto é 0
    for i in range (1, a + 1):
        if a % i == 0:

            #se contador for diferente de 2 o número não é primo
            contador += 1

    if contador == 2:
        #print(str(i) + " .")
        primos = primos + str(i) + " . "

print(primos)