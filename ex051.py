'''Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10
primeiros termos dessa progressão.'''

primeiroTermo = int(input('Informe o PRIMEIRO TERMO da Progressão Aritimética: '))
razao = int(input('Informe a RAZÃO da Progressão Aritimética:'))
for i in range(0, 10):
    print('a{} = {}'.format(i+1, primeiroTermo))
    primeiroTermo += razao
