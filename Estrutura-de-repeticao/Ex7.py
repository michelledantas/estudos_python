# A prefeitura de Quixeramubim abriu uma linha de crédito para os funcionários
# estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
# bruto. Fazer um algoritmo que permita entrar com o salário bruto e o valor da
# prestação, e informar se o empréstimo pode ou não ser concedido.

salario = float(input("Digite o salário bruto: "))
prestacao = float(input("Digite o valor da prestação: "))
limitePrestacao = salario * 0.30


if prestacao <= limitePrestacao:
    print("O empréstimo poderá ser realizado")
else:
    print("Infelizmente a prestação supera a margem. \n"
          "O empréstimo não será aprovado.")