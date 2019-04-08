'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual
foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

numeros = list(int(input('Informe um numero: '))for i in range(0, 5))
posMax = list()
posMin = list()
for i, j in enumerate(numeros):
    if max(numeros) == j:
        posMax.append(i)
    if min(numeros) == j:
        posMin.append(i)
print(f'\nO menor valor é {min(numeros)} e foram encontrados nas posições ', end='')
for i in range(0, len(posMin)):
    print(f'{posMin[i]}', end='... ')
print(f'\nO maior valor é {max(numeros)} e foram encontrados nas posições ', end='')
for i in range(0, len(posMax)):
    print(f'{posMax[i]}', end='... ')
