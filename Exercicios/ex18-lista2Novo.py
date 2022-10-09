popA = 5000000
popB = 7000000
print('pop A inicial : ' + str(popA))
print('pop B inicial : ' + str(popB))
ano  = 0
while popA < popB:
    popA = popA*1.03
    popB = popB*1.02
    print('pop A no ano ' + str(ano+1)+' -> ' + str(popA)  )
    print('pop B no ano ' + str(ano+1)+' -> ' + str(popB)  )
    ano = ano + 1
    ano += 1
print('Qtdd de anos q se passaram: ' + str(ano))
