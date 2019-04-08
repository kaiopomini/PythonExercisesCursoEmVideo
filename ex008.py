'''Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'''

n1 = float(input('Enter the measurement in meters: '))
print('The value informed is: \n {:.0f}cm \n {:.0f}mm'.format((n1*100), (n1*1000)))
