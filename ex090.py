'''Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um
dicionário. No final, mostre o conteúdo da estrutura na tela.'''

#  2.0 (com várias entradas)

alunos = list()
aluno = dict()
while True:
    aluno['nome'] = str(input('Nome: '))
    aluno['nota'] = float(input('Nota: '))
    if aluno['nota'] >= 7:
        aluno['situação'] = 'Aprovado'
    else:
        aluno['situação'] = 'Reprovado'
    alunos.append(aluno.copy())
    while True:
        opc = str(input('Deseja continuar? [S/N] ')).upper()
        if opc == 'S' or opc == 'N':
            break
        else:
            print('Opção inválida')
    if opc == 'N':
        break
print('-='*15)
for i in alunos[0]:
    print(f'{i:<10}', end='')

for k in alunos:
    print()
    for i, j in k.items():
        print(f'{j:<10}', end='')
