
print("Vamos calcular a quantidade de caixas de azulejos que será necessária para azulejar toda a cozinha.")

#entrada da metragens das paredes
largura = float(input("Digite a largura: "))
comprimento = float(input("Digite o comprimento: "))
altura = float(input("Digite a altura da parede: "))

#soma das paredes
paredesLargura = (largura * altura)*2 #pois são 2 paredes da mesma metragem
paredesComprimento = (comprimento * altura) * 2 #pois são 2 paredes da mesma metragem

#multiplicar a largura de cada parede pela altura do ambiente
areaTotal = paredesComprimento + paredesComprimento

totalAzulejo = areaTotal/2 #divido por cada caixa que possui 2 metros de azulejo

print("O total da área a ser azulejada é: " + str(areaTotal)+ ("m²"))
print("Será necessário comprar " + str(totalAzulejo) + (" caixas de azulejos."))
