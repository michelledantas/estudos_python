# 1. Faça um programa para informatizar o cadastro de produtos em uma loja.
# Você deve cadastrar produtos até o preço 0 ser cadastrado.
# Cada produto deve ser armazenado com as seguintes informações: nome, preço, quantidade e categoria (“L” para luxo e “C” para comum).
# Depois de cadastrados os produtos informe:
# - a quantidade de produtos de luxo com preço menor que R$ 2000,00 OK
# - o preço médios dos produtos de luxo
# - o nome do produto mais caro com quantidade menor que 50. OK
# - o percentual de produtos que custam entre R$ 100,0 e R$ 200,00.
# - o nome do produto comum mais barato OK

preco = 1

qtddProdLuxo = 0
qtddProdLuxoMenor2000 = 0
prodMaisCaro = ""
precoProdMaisCaro = 0
precoProdLuxo = 0
prodComumMaisBarato = ""
precoProdComumMaisBarato = 0
qtdd100e200 = 0
qtddProdTotal = 0

while preco != 0:
    #Cadastro dos produtos
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    if preco != 0:
        qtdd = int(input("Digite a qtdd: "))
        categoria = input("Digite L-luxo ou C-Comum: ")

        # - a quantidade de produtos de luxo com preço menor que R$ 2000,00 OK
        if preco < 2000 and (categoria == "L" or categoria == "l"):
            qtddProdLuxoMenor2000 = qtddProdLuxoMenor2000 + qtdd
            #print("qtddProdLuxo: " + str(qtddProdLuxoMenor2000))

        # - o preço médios dos produtos de luxo OK
        if categoria == "L" or categoria == "l":
            precoProdLuxo = precoProdLuxo + preco
            qtddProdLuxo = qtddProdLuxo + qtdd
            #print("PrecoProdLuxo: " + str(precoProdLuxo))
            #print("QtddProdLuxo" + str(qtddProdLuxo))

        # - o nome do produto mais caro com quantidade menor que 50. OK
        if preco > precoProdMaisCaro and qtdd < 50:
            prodMaisCaro = nome
            #print("prodMaisCaro " + str(prodMaisCaro))

        qtddProdTotal = qtddProdTotal + qtdd
        # - o percentual de produtos que custam entre R$ 100,0 e R$ 200,00. OK
        if preco >= 100 and preco <=200:
            qtdd100e200 = qtdd100e200 + 1

        # - o nome do produto comum mais barato OK
        if precoProdComumMaisBarato < preco and (categoria == "C" or categoria =="c"):
            prodComumMaisBarato = nome
            #print("prodComumMaisBarato" + str(prodComumMaisBarato))

print("A quantidade de produtos de luxo com preço menor que R$2000,00 é: " + str(qtddProdLuxoMenor2000))
precoMedio = precoProdLuxo/qtddProdLuxo
print("O preço médios dos produtos de luxo é: " + str(precoMedio))
print("O produto mais caro e com quantidade menor que 50 é: " + str(prodMaisCaro))
percProd100e200 = (qtdd100e200/qtddProdTotal)*100
print("O percentual dos produtos com preço entre R$100 e R$200 é: " + str(percProd100e200))
print("O produto comum mais barato é: " + str(prodComumMaisBarato))

