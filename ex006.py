'''Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.'''

n1 = float(input('Enter a number: '))
print('double the number entered is {:.0f}, the triple is {:.0f} and the square root is {:.3f}!'.format(n1*2, n1*3, n1**(1/2)))
