'''Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''

from math import cos, sin, tan, radians
a = float(input('Enter with a angle: '))
ar = radians(a)
print('the cosine of {} is {:.2f}'.format(a, cos(ar)))
print('the sine of {} is {:.2f}'.format(a, sin(ar)))
print('the tangent of {} is {:.2f}'.format(a, tan(ar)))
