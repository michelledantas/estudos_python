# Usuário digitar o dia e mês de seu aniversário e a data de hoje (dia e mês);
# em seguida, o programa deve calcular quantos dias faltam entre a data de hoje e a data do próximo aniversário.
# Suponha todos os meses com 30 dias

diaNiver = int(input("Digite o dia do seu aniversário: "))
mesNiver = int(input("Digite o mês do seu aniversário: "))
print("Seu aniversário é dia " + str(diaNiver) + "/" + str(mesNiver))

diaAtual = int(input("Digite que dia é hoje: "))
mesAtual = int(input("Digite em qual mês estamos: "))
print("Hoje é dia " + str(diaAtual) + "/" + str(mesAtual))

# dia do aniversário = dia de hoje e mes tbm
if diaNiver == diaAtual and mesNiver == mesAtual:
    print("Parabéns, hoje é o seu aniversário. \nSeu próximo aniversário será em 1 ano.")

# mês do aniversário = mês atual
elif diaNiver != diaAtual and mesNiver == mesAtual:
    # print("O mês atual é o mesmo mês do seu aniversário")
    if diaAtual < diaNiver:
        diasRestantes = diaNiver - diaAtual
        print("Faltam " + str(diasRestantes) + " dias para seu próximo aniversário")
    else:
        diasRestantes = 360 - (diaAtual - diaNiver)
        print("Faltam " + str(diasRestantes) + " dias para seu próximo aniversário")

#elif mesNiver < mesAtual:
 #   if diaNiver < diaAtual:

else:
    print("não estou conseguindo avançar")