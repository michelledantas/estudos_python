#  Faça um programa para informatizar o cadastro dos pacientes em um hospital.
# Você deve cadastrar os pacientes com as seguintes informações: nome, idade, sexo (M ou F) e peso.
# Após terminado o cadastro, perguntar se o usuário deseja cadastrar mais alunos.
# Caso ele responda “sim” outro cadastro deve ser efetuado.
# Do contrário, deve ser informado:
# - o nome do paciente mais velho e com peso maior que 50 quilos. ok
# - peso médio dos pacientes do sexo feminino com mais de 30 anos.
# - a quantidade de pacientes do sexo masculino ou com idade menor que 45 anos. ok
# - o percentual de pacientes (masculino ou feminino) que são idosos (mais de 59 anos).

resposta = 'sim'
qtddPaciente = 0
idadePacienteMaisVelho = 0
nomeDoPacienteMaisVelho = ""
pesoPacienteFemininoComMaisDeTrintaAnos = 0
qtddPacienteFemininoComMaisDeTrintaAnos = 0
pesoMedioSexoFemininoComMaisDeTrintaAnos = 0
qtddPacientesMasculinoComIdadeMenorQue45 = 0
pacientesIdososMaior59anos = 0
while resposta == 'sim':
    #cadastro de pacientes ok
    print("Paciente #" + str(qtddPaciente + 1))
    qtddPaciente = qtddPaciente + 1
    nome = input("Digite o nome do paciente: ")
    idade = int(input("Digite a idade do paciente: "))
    sexo = input("Digite o sexo do paciente, M OU F: ")
    peso = float(input("Digite o peso do paciente: "))

    #o nome do paciente mais velho e com peso maior que 50 quilos ok
    if idade > idadePacienteMaisVelho and peso >= 50:
        idadePacienteMaisVelho = idade
        nomeDoPacienteMaisVelho = nome

    # - peso médio dos pacientes do sexo feminino com mais de 30 anos.
    if (sexo == "F" or sexo == "f") and idade > 30:
        pesoPacienteFemininoComMaisDeTrintaAnos = pesoPacienteFemininoComMaisDeTrintaAnos + peso
        qtddPacienteFemininoComMaisDeTrintaAnos = qtddPacienteFemininoComMaisDeTrintaAnos + 1

    # - a quantidade de pacientes do sexo masculino ou com idade menor que 45 anos.
    if (sexo == "M" or sexo == "m") and idade < 45:
        qtddPacientesMasculinoComIdadeMenorQue45 = qtddPacientesMasculinoComIdadeMenorQue45 + 1

    # - o percentual de pacientes (masculino ou feminino) que são idosos (mais de 59 anos).
    if idade > 59:
        pacientesIdososMaior59anos = pacientesIdososMaior59anos + 1

    resposta = input("Deseja cadastrar mais pacientes (sim/não)?")

if qtddPacienteFemininoComMaisDeTrintaAnos > 0:
    pesoMedioSexoFemininoComMaisDeTrintaAnos = pesoPacienteFemininoComMaisDeTrintaAnos / qtddPacienteFemininoComMaisDeTrintaAnos
    print("O peso médio de pacientes do sexo F com mais de 30 anos é " + str(pesoMedioSexoFemininoComMaisDeTrintaAnos))


print("O paciente mais velho e com peso > 50 é: " + str(nomeDoPacienteMaisVelho))
print("Qtdd de Pacientes do sexo M com idade <45: " + str(qtddPacientesMasculinoComIdadeMenorQue45))
percentualPacientesIdososMeF = (pacientesIdososMaior59anos / qtddPaciente)*100
print("Percentual de pacientes 60 anos ou mais: " + str(percentualPacientesIdososMeF) + "%")