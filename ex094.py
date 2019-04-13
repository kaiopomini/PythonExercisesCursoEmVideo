'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

person = dict()
cad = list()
while True:
    person['name'] = str(input('NOME: '))
    while True:
        person['sex'] = str(input('SEXO: [M/F] ')).upper()
        if person['sex'] == 'M' or person['sex'] == 'F':
            break
        else:
            print('Erro! Informe apenas M ou F!')
    person['age'] = int(input('IDADE: '))
    while True:
        opc = str(input('Quer continuar? [S/N] ')).upper()
        if opc == 'S' or opc == 'N':
            break
        else:
            print('Erro! Informe apenas S ou N!')
    cad.append(person.copy())
    if opc == 'N':
        break
print(cad)
media = 0
for i, j in enumerate(cad):
    media += j['age']
media = media / (len(cad))
print(f'A) Ao todo temos {len(cad)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos.')
print('C) As mulheres cadastradas foram:', end=' ')
for i, j in enumerate(cad):
    if j['sex'] == 'F':
        print(f' {j["name"]}', end='')
        if i+1 != len(cad):
            print(',', end='')
        else:
            print('.')
print('D) Lista das pessoas que estão acima da média de idade: ')
for i in cad:
    if i['age'] > media:
        print('    ', end='')
        for k, v in i.items():
            print(f'{k} = {v}', end='; ')
        print()
