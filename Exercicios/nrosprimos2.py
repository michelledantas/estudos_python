n = int(input('Digite o número: '))

print('Percorrendo nos n numeros....')
for i in range(2,n,1):

    primo = True
    for j in range (2,i,1):
        if i%j == 0:
#            print('entrou no if i%j : ' + str(i) + '%' + str(j))
            primo = False
    if primo == True:
        print(i)


print('Fim da exibição dos numeros')

#primo = True
#for i in range(2,n,1):
#    if n%i == 0: #significa que o número n é divisível por i, ou seja, nro nao primo
#        primo = False

#if primo == True:
#    print('Numero é primo')
#else:
#    print('Numero não é primo')
