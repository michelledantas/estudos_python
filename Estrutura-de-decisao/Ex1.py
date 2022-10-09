print("Olá, seja bem vindo ao meu programa")
nro1 = int(input("Digite o primeiro número: "))
nro2 = int(input("Digite o segundo número: "))

print ("Vamos descobrir qual número é o maior: ")

#nro1 > nro2?
if nro1 > nro2:
    print ("O número " + str(nro1) + " é maior que o número " + str(nro2))

elif nro2 > nro1:
    print ("O número " + str(nro2) + " é maior que o número " + str(nro1))
else:
    print("Não existe número maior, os números digitados são iguais3")
