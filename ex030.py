'''Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''

n = int(input('Informe um numero inteiro: '))
if (n % 2) == 1:
    print('o numero {} é IMPAR.'.format(n))
else:
    print('o numero {} é PAR.'.format(n))
