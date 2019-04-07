from random import randrange
numeros = tuple(randrange(1000) for i in range(5))

print(f'Os numeros sorteados foram: {numeros}')
print(f'O maior numero é: {max(numeros)}')
print(f'O menor numero é: {min(numeros)}')
