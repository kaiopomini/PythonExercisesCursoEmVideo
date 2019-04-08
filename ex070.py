'''Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''

total = contador = 0
firstRun = True
while True:
    nome = str(input('Infome o nome do produto: '))
    valor = float(input('Informe o valor do produto: R$'))
    total += valor
    if firstRun:
        menor = valor
        nomemenor = nome
        firstRun = False
    else:
        if valor < menor:
            menor = valor
            nomemenor = nome
    if valor > 1000:
        contador += 1
    while True:
        continuar = str(input('Gostaria de continuar? [S/N] ').strip().upper())
        if continuar == 'N':
            break
        elif continuar == 'S':
            break
    if continuar == 'N':
        break
print('FIM DA COMPRA')
print(f'O total da compra foi de R${total:.2f}')
print(f'A quantidade de produtos que custaram mais de R$1000.00 foi {contador}')
print(f'O produto mais barato foi "{nomemenor}" que custou R${menor:.2f}')
