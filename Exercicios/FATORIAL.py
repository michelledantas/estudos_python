# Faça um programa para calcular o fatorial de um número.
# O usuário deve informar o número para calcular o fatorial.
# O programa, deve exibir uma string com a operação e depois o resultado.

# Exemplo: Calcular fatorial de : 6

# 6!= 1*2*3*4*5*6 6!= 720

n = int(input("Digite um número: "))
fatorial = ("{}!= ").format(n)
result = 1
i = n-1

for i in range (1,n+1):
    result = result * i
    if i==n:
        fatorial += ("{}= {}").format(i,result)
    else:
        fatorial += ("{}*").format(i)
print(fatorial)
