#alunos = []
#for i in range(4):
#    nomeAluno = input('Digite o nome do aluno: ')
#    alunos.append(nomeAluno)

#print(alunos)

produtos = []
continuar = 'sim'
while continuar == 'sim':
    nomeProduto = input("Digite o nome do produto: ")
    produtos.append(nomeProduto)
    continuar = input("Deseja continuar (sim/nao) ?")

print('Lista de produtos: ')
qtddElementos = len(produtos)
print('Qtdd de produtos cadastrados: ' + str(qtddElementos))
contador = 1
for elemento in produtos: #para cada elemento na lista de produtos:
    print('Produto #'+str(contador) + ' - ' + elemento)
    contador = contador + 1

