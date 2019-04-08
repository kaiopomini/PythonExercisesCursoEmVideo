'''Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''

h = float(input('Enter with the height of the wall: '))
w = float(input('Enter with the width of the wall: '))
print('You need to paint the wall {:.2f} liters of wall paint.'.format((h*w)/2))
