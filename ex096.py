'''
Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno.
'''


def area(larg, comp):
    print(f'A área de um terreno de {larg:.2f} x {comp:.2f} é de {larg*comp:.2f}m2.')


a = int(input('Largura (m): '))
b = int(input('Comprimento (m): '))
area(a, b)
