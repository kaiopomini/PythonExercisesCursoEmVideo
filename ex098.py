'''
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim
e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''

from time import sleep


def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p = (-p)
    print('#' * 50)
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    if i <= f:
        while i <= f:
            print(f'{i} ', end='')
            sleep(0.3)
            i += p
    else:
        while i >= f:
            print(f'{i} ', end='')
            sleep(0.3)
            i -= p
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('#'*50)
print('Agora é sua vez de personalizar a contagem!')
a = int(input('Inicio: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contador(a, b, c)
