'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma
lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

numeros = list()
for i in range(0, 5):
    aux = int(input('Digite um número: '))
    if len(numeros) == 0:
        numeros.append(aux)
        print('Primeiro item da lista...')
    else:
        if max(numeros) <= aux:
            numeros.append(aux)
            print('Adicionado ao final da lista...')
        else:
            for j in range(0, len(numeros)):
                if numeros[j] > aux:
                    numeros.insert(j, aux)
                    print(f'Adicionado a posição {j} da lista...')
                    break
print(f'Os valores digitados em ordem foram {numeros}')
