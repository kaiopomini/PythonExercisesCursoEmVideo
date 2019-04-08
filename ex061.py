'''Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10
 primeiros termos da progressão usando a estrutura while.'''

primeiroTermo = int(input('Informe o PRIMEIRO TERMO da Progressão Aritimética: '))
razao = int(input('Informe a RAZÃO da Progressão Aritimética:'))
contador = 1
while contador <= 10:
    print('a{} = {}'.format(contador, primeiroTermo))
    primeiroTermo += razao
    contador += 1
