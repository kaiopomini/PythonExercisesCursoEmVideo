primeiroTermo = int(input('Informe o PRIMEIRO TERMO da Progressão Aritimética: '))
razao = int(input('Informe a RAZÃO da Progressão Aritimética:'))
for i in range(0, 10):
    print('a{} = {}'.format(i+1, primeiroTermo))
    primeiroTermo += razao
