'''Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".'''

n = str(input('Informe o nome da sua cidade: '))
nsplit = n.strip().split()
print('Sua cidade começa com "santo"? {}'.format('SANTO' in nsplit[0].upper()))
