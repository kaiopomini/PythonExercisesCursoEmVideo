primeiroTermo = int(input('Informe o PRIMEIRO TERMO da Progressão Aritimética: '))
razao = int(input('Informe a RAZÃO da Progressão Aritimética:'))
contador = 1
while contador <= 10:
    print('a{} = {}'.format(contador, primeiroTermo))
    primeiroTermo += razao
    contador += 1
