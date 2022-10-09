from random import randint

pessoas = []
jovens = 0
idosos = 0
semRisco = 0
tamanhoPopulacao = 50
menor50anos = 0
entre50e59 = 0
entre60e69 = 0
entre70e79 = 0
maior80 = 0
for i in range(tamanhoPopulacao):
    idade = randint (1,99)
    if idade < 20:
        jovens =jovens + 1
    if idade > 60:
        idosos = idosos + 1
    if idade < 10:
        semRisco = semRisco + 1

    #calcular a qtdd em cada faixa:
    if idade <50:
        menor50anos = menor50anos + 1
    elif idade <=59:
        entre50e59 = entre50e59 + 1
    elif idade >=60 and idade <= 69:
        entre60e69 = entre60e69 + 1
    elif idade >=70 and idade < 79:
        entre70e79 = entre70e79 + 1
    else:
        maior80 = maior80 + 1
    pessoas.append(idade)


print('Jovens: ' + str(jovens))
percentual = idosos/tamanhoPopulacao
print('Percentual idosos: ' + str(percentual))
percentual = semRisco/tamanhoPopulacao
print('Percentual da populacao sem risco: ' + str(percentual))

#Enquanto entre
# 0 e 49 anos ela não passa de 1%,
# entre 50 e 59 fica em 1,3%,
# entre 60 e 69 vai para 3,6%,
# entre 70 e 79 anos sobe para 8%
# e acima dos 80 chega a 14,8%
prob = (entre50e59*1.3+ entre60e69*3.6 + entre70e79*8+maior80*14.8)/tamanhoPopulacao
print('probabilidade: ' + str(prob))

print(pessoas)
