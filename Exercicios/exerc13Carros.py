qtddCarros = int(input('Digite a qtdd de carros: '))

comissao = 0
comissaoTotal = 0
valorMaisCaro = 0
modeloMaisCaro = ''
qtddCarrosEntre20Ke30K = 0
somaPrecoCarros = 0
for i in range (qtddCarros):
    print("Digite os dados do carro #" + str(i+1))
    valor = float(input('Digite o valor do carro: '))
    modelo = input('Digite o modelo do carro: ')

    #comissao:
    if valor <= 10000:
        comissao = valor * 0.10
    else:
        comissao = valor * 0.11
    comissaoTotal = comissaoTotal + comissao

    #O modelo do carro mais caro.
    if valor > valorMaisCaro: #encontrei um carro mais caro
        valorMaisCaro = valor
        modeloMaisCaro = modelo

    #A quantidade de carros que custam mais que R$20.000,00
    # e menos que R$30.000,00.
    if valor > 20000 and valor < 30000:
        qtddCarrosEntre20Ke30K = qtddCarrosEntre20Ke30K + 1

    #O preço médio dos carros.
    somaPrecoCarros = somaPrecoCarros + valor

#exibindo resultados:
print("Total de comissao: " + str(comissaoTotal))
print("O carro mais caro é o " + modeloMaisCaro)
print('Qtdd carros entre 20k e 30k : '+ str(qtddCarrosEntre20Ke30K))
precoMedio = somaPrecoCarros/qtddCarros
print('Preco medio dos carros: ' + str(precoMedio))
