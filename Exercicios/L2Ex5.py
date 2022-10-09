#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
# Faça um programa que gere a série até que o valor seja maior que 500.

print("Vamos exibir a série Fibonacci até que o valor seja maior que 500")

primeiroTermo = 0
segundoTermo = 1
proxTermo = primeiroTermo + segundoTermo
serieTexto = str(primeiroTermo)+ "," + str(segundoTermo)

while proxTermo < 500:
    primeiroTermo = segundoTermo
    segundoTermo = proxTermo
    proxTermo = primeiroTermo + segundoTermo
    serieTexto = serieTexto + "," + str(proxTermo)
print(serieTexto + ".")