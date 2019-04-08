'''Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

n1 = float(input('informe o primeiro numero: '))
n2 = float(input('informe o segundo numero: '))
n3 = float(input('informe o terceiro numero: '))
menor = n1
maior = n1
# testa quem é menor
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# testa quem é maior
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('o menor numero é {:.2f}'.format(menor))
print('o maior numero é {:.2f}'.format(maior))

'''
#1.0

if n1 >= n2:
    if n1 >= n3:
        print('o maior numero é {:.2f}'.format(n1))
    else:
        print('o maior numero é {:.2f}'.format(n3))
else:
    if n2 >= n3:
        print('o maior numero é {:.2f}'.format(n2))
    else:
        print('o maior numero é {:.2f}'.format(n3))
if n1 <= n2:
    if n1 <= n3:
        print('o menor numero é {:.2f}'.format(n1))
    else:
        print('o menor numero é {:.2f}'.format(n3))
else:
    if n2 <= n3:
        print('o menor numero é {:.2f}'.format(n2))
    else:
        print('o menor numero é {:.2f}'.format(n3))
'''
