
nomeMaisVelho = ''
idadeMaisVelho = 0
somaPesoMulheresMais30 = 0
qtddMulheresMais30 = 0
qtddHomensMenor45 = 0
qtddIdoso = 0
qtddPacientes = 0

resposta  = 'sim'
while resposta == 'sim':
    nome = input('Digite o nome do paciente: ')
    sexo = input('Digite o sexo (M/F) do paciente: ')
    idade = int(input('Digite a idade do paciente: '))
    peso = float(input('Digite o peso do paciente: '))
    resposta = input('Deseja continuar (sim/nao) ?')
    #o nome do paciente mais velho e com peso maior que 50 quilos.
    if peso > 50:  # if peso > 50 and idade > idadeMaisVelho:
        if idade > idadeMaisVelho:
            idadeMaisVelho = idade
            nomeMaisVelho = nome

    #- peso médio dos pacientes do sexo feminino com mais de 30 anos
    if (sexo == 'F' or sexo == 'f') and idade > 30:
        somaPesoMulheresMais30 = somaPesoMulheresMais30+peso
        qtddMulheresMais30 = qtddMulheresMais30 + 1


    #- a quantidade de pacientes do sexo masculino ou com idade menor que 45 anos.
    if (sexo == 'm' or sexo == 'M') or idade < 45:
        qtddHomensMenor45 = qtddHomensMenor45 + 1

    #o percentual de pacientes (masculino ou feminino) que são idosos (mais de 59 anos).
    if idade > 59:
        qtddIdoso = qtddIdoso + 1
    qtddPacientes = qtddPacientes + 1

print('paciente mais velho com mais de 50kg: ' + nomeMaisVelho)

#calculo da media de peso de mulher com mais de 30
if qtddMulheresMais30 > 0:
    media = somaPesoMulheresMais30/qtddMulheresMais30
    print('Media de peso de mulher com mais de 30anos: '+ str(media))

print('quantidade de pacientes do sexo masculino ou com idade menor que 45 anos: ' + str(qtddHomensMenor45))

if qtddPacientes > 0:
    percentual = qtddIdoso/qtddPacientes
    print('percentual : ' + str(percentual))
