listaNome = []
listaProva = []
listaTrabalho = []
listaFrequencia = []
listaMedia = []
listaMediaMaior8 = []
mediaAtualizada = False
opcao = -1
while opcao != 0:
    print('MENU')
    print('0 - Sair')
    print('1 - Cadastrar Aluno')
    print('2 - Listar Alunos')
    print('3 - Calcular e exibir medias')
    print('4 - Dado o nome de um aluno, exibir sua média')
    print('5 - Criar lista com nome de alunos com media maior que 8')
    print('6 - Exibir o status de cada aluno')
    opcao = int(input('Escolha uma opcao: '))
    if opcao == 1:
        nome = input('Digite o nome: ')
        prova = float(input('Digite a nota da prova: '))
        trabalho = float(input('Digite a nota do trabalho: '))
        freq = float(input('Digite a frequencia do aluno: '))
        listaNome.append(nome)
        listaProva.append(prova)
        listaTrabalho.append(trabalho)
        listaFrequencia.append(freq)
        mediaAtualizada = False
    elif opcao ==2:
        qtddAlunos = len(listaNome)
        for i in range(qtddAlunos):
            print("Aluno #" + str(i+1))
            print('Nome: ' + listaNome[i])
            print('Nota Prova: ' + str(listaProva[i]))
            print('Nota Trabalho : ' +str(listaTrabalho[i]))
            print('Frequencia: ' + str(listaFrequencia[i]))
    elif opcao == 3:
        qtddAlunos = len(listaFrequencia) #poderia ser qlq lista já criada
        for i in range(qtddAlunos):
            media  = listaProva[i]*0.7 + listaTrabalho[i]*0.3
            listaMedia.append(media)
            print('Aluno : ' + listaNome[i] + ' -> ' + str(media))
        mediaAtualizada = True
    elif opcao ==4:
        nomeAluno = input('Digite o nome do aluno para buscarmos sua media: ')
        qtddAlunos = len(listaTrabalho)
        existeAluno = False #considero que o aluno nao existe
        for i in range(qtddAlunos):
            if nomeAluno == listaNome[i]:
                existeAluno = True #registrando que o aluno existe na lista
                if len(listaMedia) > 0: #significa que a listaMedia já foi criada
                   print('Media do aluno: ' + str(listaMedia[i]))
                else: #se a lista nunca foi criada ainda, preciso calcular:
                   media  = listaProva[i]*0.7 + listaTrabalho[i]*0.3
                   print('Media do aluno: ' + str(media))
        if not existeAluno:
            print('Nao existe aluno cadastrado com esse nome!')
    elif opcao == 5:
        qtddAlunos = len(listaTrabalho)
        if mediaAtualizada: #significa que a lista media já foi gerada e está atualizada!
            listaMediaMaior8 = []
            for i in range(qtddAlunos):
                if listaMedia[i] > 8:
                    listaMediaMaior8.append(listaNome[i])
            print(listaMediaMaior8)
        else:
            print('Antes de gerar a lista é preciso chamar a opcao 3 do menu!')

    elif opcao == 6:
        qtddAlunos = len(listaNome)
        if mediaAtualizada:
            for i in range(qtddAlunos):
                print('Aluno #'+ str(i+1))
                print('Nome:' + listaNome[i])
                if listaMedia[i]>=6 and listaFrequencia[i]>=75:
                    print('APROVADO!')
                #•	IFA: 4 <= média final < 6 e frequência >=75%
                elif listaMedia[i]>=4 and listaMedia[i]<6 and listaFrequencia[i]>=75:
                    print('IFA')
                else:
                    print('REPROVADO')
        else:
            print('Antes de exibir o status é preciso chamar a opcao 3 do menu')
