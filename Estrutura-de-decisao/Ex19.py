#  Um motorista de de taxi deseja calcular o rendimento de seu carro na praça.
# Sabendo-se que o preço do combustível é de R$2,50, escreva um programa para ler:
# - a marcação do odômetro no início do dia
# - a marcação no final do dia
# - o número de litros de combustível gasto
# - o valor total (R$) recebido dos passageiros.
# Calcule e escreva a média do consumo em Km/l e o lucro líquido do dia. Se o
# lucro líquido no dia for inferior a R$ 100,00 exiba a mensagem que o
# taxista precisa melhorar seu desempenho.

odometroInicial = int(input("Digite a marcação do odômetro no início do dia: ")) #0
odometroFinal = int(input("Digite a marcação do odômetro no final do dia: ")) #480
litrosGasto = int(input("Digite o número de litros de combustível gasto: ")) #30
valorRecebido = int(input("Digite o valor recebido dos passageiros: ")) #150
valorCombustivel = float(input("Digite o valor do combustivel: "))
# A razão do consumo médio pode ser escrita da seguinte maneira:
# CM = S/V
# CM = consumo médio;
# S = distância percorrida em quilômetros;
# v = quantidade de combustível utilizada em litros.

kmPercorrida = odometroFinal - odometroInicial
print(type(kmPercorrida))
consumoMedio = kmPercorrida / litrosGasto

print("A média do consumo é " + str(consumoMedio) + " Km/l")

valorGastoDeCombustivel = consumoMedio * valorCombustivel
lucroLiquido = valorRecebido - consumoMedio

print("O valor gasto com combustível no dia é R$" + str(valorGastoDeCombustivel))

if lucroLiquido < 100:
     print("O taxista precisa melhorar seu desempenho. ")
else:
    print("O lucro líquido foi R$" + str(lucroLiquido))