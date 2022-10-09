listaNome = []
listaPreco = []
listaEstoque = []

opcao  = -1
while opcao !=0:
    print("menu")
    print(" 0 = sair")
    print(" 1 = cadastrar produtos")
    print(" 2 = listar produtos")
    print(" 3 = encontrar o produto mais caro")
    print(" 4 = encontrar o valor total do estoque")
    opcao = int(input("Digite a opcao : "))
    if opcao == 1:
        nome = input("Digite o nome: ")
        preco = float(input("Digite o preco: "))
        qtddEstoque = int(input("Digite a qtdd em estoque: "))
        listaNome.append(nome)
        listaPreco.append(preco)
        listaEstoque.append(qtddEstoque)
    elif opcao ==2:
        qtddProdutos  = len(listaEstoque) #ver qtos elementos foram cadastrados
        for i in range(qtddProdutos):
            print("Produto #" + str(i+1))
            print('Nome: ' + listaNome[i])
            print('Preco: ' + str(listaPreco[i]))
            print('Qtdd em estoque: ' + str(listaEstoque[i]))
    elif opcao ==3:
        maisCaro = 0
        indiceMaisCaro = - 1 #será o indice onde foi encontrado o produto mais caro
        indice = 0
        for preco in listaPreco:
            if preco > maisCaro:
                maisCaro = preco
                indiceMaisCaro = indice
            indice = indice + 1
        print('Produto mais caro: ' + listaNome[indiceMaisCaro] )
        print('Valor do produto mais caro: ' + str(maisCaro))
    elif opcao == 4:
        qtddProdutos = len(listaPreco) #ver qtos elementos foram cadastrados
        totalEstoque = 0
        for i in range(qtddProdutos):
            totalEstoque = totalEstoque + listaPreco[i]*listaEstoque[i]
        print("Total em estoque: " + str(totalEstoque))


