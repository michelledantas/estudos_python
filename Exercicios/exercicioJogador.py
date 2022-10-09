qtddJogador = 0
resposta = 'sim'
somaIdadeCorinthiansMaior80kg = 0
qtddCorinthiansMaior80kg = 0
qtddJogadoresMenor20anos = 0
while resposta == 'sim':
    print("Jogador #" + str(qtddJogador+1))
    nome = input("Digite o nome do jogador: ")
    idade = int(input("Digite a idade do jogador: "))
    peso = float(input("Digite o peso do jogador: "))
    time = input("Digite o time do jogador: ")

    #média de idade dos jogadores do “corinthians” com mais de 80 quilos.
    if time == 'corinthians' and peso > 80:
        somaIdadeCorinthiansMaior80kg = somaIdadeCorinthiansMaior80kg + idade
        qtddCorinthiansMaior80kg =qtddCorinthiansMaior80kg + 1

    if idade <20:
        qtddJogadoresMenor20anos = qtddJogadoresMenor20anos + 1
    qtddJogador = qtddJogador + 1
    resposta = input("Deseja continuar (sim/nao) ?")

if qtddCorinthiansMaior80kg>0:
    mediaIdadeCorinthiansMaior80kg = somaIdadeCorinthiansMaior80kg/qtddCorinthiansMaior80kg
    print("Media idade jog.Corinthians com mais de 80kg: "+str(mediaIdadeCorinthiansMaior80kg))
percJogadoresMenor20anos = (qtddJogadoresMenor20anos/qtddJogador)*100
print("Percentual jogadores com menos de 20 anos: " + str(percJogadoresMenor20anos))
