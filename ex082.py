'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas
listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre
o conteúdo das três listas geradas.'''

numeros = list()
impar = list()
par = list()
while True:
    a = int(input('Digite um valor: '))
    numeros.append(a)
    while True:
        parada = str(input('Quer continuar? [S/N] ')).upper()
        if (parada != 'S') and (parada != 'N'):
            print('Opção inválida!')
        else:
            break
    if parada == 'N':
        break
for i in numeros:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print(f'Os numeros digitados foram: {numeros}')
print(f'Os numeros IMPARES são: {impar}')
print(f'Os numeros PARES são {par}')
