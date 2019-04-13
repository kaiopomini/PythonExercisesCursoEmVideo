'''Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
 inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''


def maior(* num):
    print('#'*50)
    if len(num) > 0:
        for i in range(0, len(num)):
            print(f'{num[i]} ', end='')
    print(f'Foram informados {len(num)} valores ao todo.')
    if len(num) > 0:
        print(f'O maior valor informado foi {max(num)}')


maior(1, 2, 45, 34, 44, 474, 1, -2, 31)
maior(5, 55, 14, 98)
maior()
maior(5)
