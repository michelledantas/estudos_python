#Duas fabricantes de calçado disputam o mercado no Brasil.
#A empresa A tem produção de 10.000 pares/mês e um crescimento mensal de 15%.
#A empresa B, de 8.000 pares/mês e tem um crescimento mensal de 20%.
#Determinar o número de meses necessários para que a empresa B supere o número de pares produzidos pela empresa A.

producaoEmpresaA = 10000
producaoEmpresaB = 8000
n = 0 #número de meses

while producaoEmpresaB < producaoEmpresaA:
    producaoEmpresaA = producaoEmpresaA * 1.15
    producaoEmpresaB = producaoEmpresaB * 1.20
    print("Produção no mês " + str(n))
    #print("Empresa A " + str(producaoEmpresaA))
    #print("Empresa B " + str(producaoEmpresaB))
    n = n + 1

print("O número de meses necessários para que a empresa B supere o número de pares " + str(n))