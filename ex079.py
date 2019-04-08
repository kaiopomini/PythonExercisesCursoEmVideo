'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
digitados, em ordem crescente. '''

numeros = list()
while True:
    a = int(input('Digite um valor: '))
    if a in numeros:
        print('Valor duplicado! Não vou adicionar...')
    else:
        numeros.append(a)
        print('Valor adcionado com sucesso...')
    while True:
        parada = str(input('Quer continuar? [S/N] ')).upper()
        if (parada != 'S') and (parada != 'N'):
            print('Opção inválida!')
        else:
            break
    if parada == 'N':
        break
numeros.sort()
print('='*50)
print(f'Você digitou os valores {numeros}')
