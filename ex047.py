'''Exercício Python 047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.'''

print('Os números pares entre 1 e 50 são: ')
for i in range(1, 51):
    if (i % 2) == 0:
        print(i, end=' ')
