'''Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e
somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a
soma entre todos os valores pares sorteados pela função anterior.'''


from random import randint
from time import sleep


def sorteia(lst):
    print('Sorteando os valores da lista: ', end='')
    for i in range(0, 5):
        lst.append(randint(0, 999))
        sleep(0.5)
        print(f'{lst[i]} ', end='')
    print('Pronto!')


def somaPar(lst):
    soma = 0
    for i in lst:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores PARES de {lst} temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)
