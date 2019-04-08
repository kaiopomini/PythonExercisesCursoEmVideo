'''Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.'''

n = str(input('informe seu nome completo'))
nsplit = n.split()
njoin = ' '.join(nsplit)
print('Seu primeiro nome é: {}'.format(nsplit[0]))
print('Seu ultimo nome é: {}'.format(nsplit[njoin.count(' ')]))
