'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

numeros = list()
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
print(f'Foram digitados {len(numeros)} numeros...')
numeros.sort(reverse=True)
print(f'A lista digitada em ordem decrescente é {numeros}')
if 5 in numeros:
    print('O numero 5 ESTÁ na lista...')
else:
    print('O numero 5 NÃO está na lista...')
