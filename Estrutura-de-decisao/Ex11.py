
#Escreva um algoritmo que leia um número
numero = int(input("Digite um número: "))

if numero != 0:
    #Se o resultado for igual a 0, ele é divisivel por 10
    if numero % 10 == 0:
        print("O número " + str(numero) + " é divisivel por 10")
    else:
        print("O número " + str(numero) + " não é divisivel por 10")

    # Se o resultado for igual a 0, ele é divisivel por 5
    if numero % 5 == 0:
        print("O número " + str(numero) + " é divisivel por 5")
    else:
        print("O número " + str(numero) + " não é divisivel por 5")

    # Se o resultado for igual a 0, ele é divisivel por 2
    if numero % 2 == 0:
        print("O número " + str(numero) + " é divisivel por 2")
    else:
        print("O número " + str(numero) + " não é divisivel por 2")
else:
    #Eu coloquei desse forma pensando se a pessoa digitar o número 0
    print("Não é possível realizar a conta com o número digitado.")


