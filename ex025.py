'''Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''

n = str(input('Informe seu nome completo: '))
print('Seu nome contem silva? {}'.format('SILVA' in n.upper()))
