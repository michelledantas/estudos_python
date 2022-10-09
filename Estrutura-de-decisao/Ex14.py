#Crie um algoritmo que leia a idade de uma pessoa e informe a sua classe eleitoral:

idade = int(input("Digite sua idade: "))

#a. não eleitor (abaixo de 16 anos);
if idade < 16:
    print("Você ainda não é eleitor. ")

#b. eleitor obrigatório (entre a faixa de 18 e menor de 65 anos);
elif idade >=18 and idade <65:
    print("Você tem a obrigação de votar. ")

#c. eleitor facultativo (eleitor entre 16 até 18 anos ou eleitor maior de 65 anos, inclusive).
else: print("Você é um eleitor facultativo. ")