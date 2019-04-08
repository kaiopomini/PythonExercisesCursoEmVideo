'''Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
 mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randrange
numeros = tuple(randrange(1000) for i in range(5))

print(f'Os numeros sorteados foram: {numeros}')
print(f'O maior numero é: {max(numeros)}')
print(f'O menor numero é: {min(numeros)}')
