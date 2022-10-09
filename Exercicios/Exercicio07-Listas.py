lista1 = []
lista2 = []
listaUniao = []
listaUniaoSemRep = []
contLista1 = 0
opcao = -1
tamanhoLista1 = 0
tamanhoLista2 = 0
while opcao !=0:
    print('Menu')
    print('1 - Inserir elemento na lista 1')
    print('2 - Inserir elementos na lista 2')
    print('3 - Exibir conteudo das listas')
    print('4 - Lista Uniao')
    print('44 - Uniao sem repetição')
    print('5 - Interseccao')
    print('6 - encontrar o maior valor das duas listas e somar esse valor aos elementos da primeira lista')
    print('7 -  multiplicar os elementos de cada posição da primeira lista pelo valor do elemento na segunda lista, criando e exibindo uma nova lista')
    opcao  = int(input('Digite a opcao : '))
    if opcao == 1:
        if contLista1 < 5:
            nro = int(input('Digite o elemento da lista 1: '))
            lista1.append(nro)
            contLista1 = contLista1 + 1
            tamanhoLista1 = contLista1
            print('Lista 1: ')
            print(lista1)
        else:
            print('Ja existem 5 elementos na lista 1')
    elif opcao == 2:
        nro = int(input('Digite o primeiro nro da lista: '))
        lista2.append(nro)
        for i in range (4):
            novoNumero = lista2[i]*2
            lista2.append(novoNumero)
        print(lista2)
    elif opcao ==3:
        print('Lista 1')
        print(lista1)
        print('Lista 2')
        print(lista2)
    elif opcao == 4:
       listaUniao = lista1 + lista2
       print(listaUniao)
    elif opcao == 44:
        tamanhoLista1 = len(lista1)
        listaUniaoSemRep = []
        #colocar os elementos da lista 1 na lista uniaoSemRep
        for i in range(tamanhoLista1):
           listaUniaoSemRep.append(lista1[i])
        #percorrer todos os elementos da lista 2 e verificar
        #se ele está na lista uniao. Se estiver nao vou inserir
        #novamente. Se nao estiver na lista ainda eu vou inserir
        tamanhoLista2 = len(lista2)
        for indice2 in range(tamanhoLista2): #percorrendo a lista2
           existe = False
           for indice1 in range(tamanhoLista1): #percorrendo a lista 1
                if lista1[indice1] == lista2[indice2]:
                    existe = True
           #quando eu sair do for acima existe vale True se eu encontrei
           #o valor da lista2 na lista 1. Vale false caso contrario

           if existe == False:
               listaUniaoSemRep.append(lista2[indice2])
        print(listaUniaoSemRep)
    elif opcao ==5:
        listaInterseccao = []
        tamanhoLista1 = len(lista1)
        tamanhoLista2 = len(lista2)
        for indice1 in range(tamanhoLista1):
            existe = False
            for indice2 in range(tamanhoLista2):
                if lista1[indice1] == lista2[indice2]:
                    existe = True
            if existe:
                listaInterseccao.append(lista1[indice1])
        print(listaInterseccao)
    elif opcao == 6:
        maiorValor = -1
        listaUniao = lista1 + lista2
        tamanhoUniao = len(listaUniao)
        for i in range(tamanhoUniao):
            if listaUniao[i] > maiorValor:
                maiorValor = listaUniao[i]
        print("Maior valor: " + str(maiorValor))
        print(lista1)
        for i in range (len(lista1)):
            lista1[i] = lista1[i] + maiorValor
        print(lista1)
    elif opcao ==7:
        tamanhoLista1 = len(lista1)
        tamanhoLista2 = len(lista2)
        novaLista = []
        if tamanhoLista1 == tamanhoLista2:
            for i in range (tamanhoLista1):
                valor = lista1[i]*lista2[i]
                novaLista.append(valor)
        print(novaLista)
    elif opcao == 8:
        lista1 = []
        lista2 = []
