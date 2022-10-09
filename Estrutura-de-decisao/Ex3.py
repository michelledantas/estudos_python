#Qual o tamanho do lote
comprimento = float(input("Digite o comprimento do lote: "))
largura = float(input("Digite a largura do lote: "))

#calcula e exibe quantos metros quadrados tem o lote
metroQuadrado = float(comprimento * largura)
print ("O lote possui " + str(metroQuadrado) + "m²")

cidade = int(input("Escolha a opção da localização do lote: 1 - Curitiba/PR ou 2 - São Paulo/SP "))

#se estiver em Curitiba custará R$450,00 o metro quadrado
if cidade == 1:
    print("Lote localizado em Curitiba/PR")
    #metroQuadrado = float(comprimento * largura)
    valor = metroQuadrado * 450.00
    print("O valor do lote é R$" + str(valor))

#se estiver em São Paulo custará R$ 500,00 o metro quadrado
elif cidade == 2:
    print("Lote localizado em São Paulo/SP")
    valor = metroQuadrado * 500
    print("O valor do lote  é R$" + str(valor))
else:
    print("Opção inválida ")