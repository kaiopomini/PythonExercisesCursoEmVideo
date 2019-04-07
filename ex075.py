numeros = tuple(int(input('Informe um numero de 0 a 10: ')) for i in range(4))

print(numeros)
pos = ''
quantidade = aux = 0
for i in range(len(numeros)):
    if int(numeros[i]) == 9:
        quantidade += 1
    if aux == 0:
        if int(numeros[i]) == 3:
            pos = i
            aux += 1

pares = ', '.join(str(i) for i in numeros if i % 2 == 0)

if pos == '':
    print('nao foi encontrado o numero 3')
else:
    print(f'O primeiro numero 3 está na posição {pos + 1}')
print(f'Foram encontrados {quantidade} numeros 9')
print(f'Os numeros pares digitados são {pares}.')

'''


auxiliar = ('um', 'outro', 'mais', 'o último')
valores = tuple(int(input(f'Digite {auxiliar[n]} número: ')) for n in range(4))
pares = ' '.join(str(_) for _ in valores if _ % 2 == 0)
print(f'Você digitou os valores {valores}\n'
      f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 not in valores:
    print('O valor 3 não foi digitado em nenhuma vez.')
else:
    tres = valores.index(3) + 1
    print(f'O valor 3 apareceu na {tres}ª posição')
if pares:
    print(f'Os valores pares digitados foram {pares}')
else:
    print('Nenhum número par foi digitado')

'''
