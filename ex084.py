''' Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves. '''

leitura = list()
pessoas = list()
pessoasLeves = list()
pessoasPesadas = list()
maior = menor = 0
while True:
    leitura.append(str(input('Informe o nome: ')))
    leitura.append(float(input('Informe o peso em KG: ')))
    pessoas.append(leitura[:])
    leitura.clear()
    while True:
        opc = str(input('Você deseja continuar?: [S/N]')).upper()
        if opc == 'S' or opc == 'N':
            break
        else:
            print('Opção inválida!')
    if opc == 'N':
        break
maior = menor = pessoas[0][1]  # atribui o primeiro maior e menor

for i in pessoas:  # busca o maior e menor
    if i[1] > maior:
        maior = i[1]
    if i[1] < menor:
        menor = i[1]

for i in pessoas:  # atribui a lista de maior e menor / dá pra colocar no print para não usar outra lista (2.0)
    if i[1] == maior:
        pessoasPesadas.append(i[0])
    if i[1] == menor:
        pessoasLeves.append(i[0])


print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi {maior:.1f}Kg. Peso de {pessoasPesadas}')
print(f'O menor peso foi {menor:.1f}Kg. Peso de {pessoasLeves}')
