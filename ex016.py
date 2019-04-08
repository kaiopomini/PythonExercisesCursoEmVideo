'''Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.'''

from math import trunc
n1 = float(input('Enter with a number: '))
print('the integer part of {} is: {}'.format(n1, (trunc(n1))))
