'''
Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista
única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem
crescente.
'''

numeros = [[], []]

for i in range(0, 7):
    aux = int(input('Informe um numero: '))
    if aux % 2 == 0:
        numeros[0].append(aux)
    else:
        numeros[1].append(aux)

numeros[0].sort()
numeros[1].sort()

print(f'Os numeros pares são {numeros[0]}')
print(f'Os numeros impares são {numeros[1]}')