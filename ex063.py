'''Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
elementos de uma Sequência de Fibonacci.

Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8'''

n = int(input('informe a quantidade da sequencia fibonaci: '))
contador = a = b = 0
r = 1

while contador < n:
    if contador != (n-1):
        print(r, end=', ')
    else:
        print(r)
    b = a
    a = r
    r = a + b
    contador += 1
