numero = int(input('Informe um numero inteiro: '))
contDivisores = 0
for i in range(1, numero+1):
    if(numero % i) == 0:
        contDivisores += 1
if contDivisores == 2:
    print('O numero {} é primo.'.format(numero))
else:
    print('O numero {} não é primo.'.format(numero))
