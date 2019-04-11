'''
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
individualmente.
'''

alunos = list()


while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    while True:
        print()
        opc = str(input('Deseja continuar? [S/N] ')).upper()
        print()
        if opc == 'S' or opc == 'N':
            break
        else:
            print('Opção inválida')
    if opc == 'N':
        break
print('='*20)
print(f'{"No.":<3} {"NOME":<10} {"MÉDIA":<4}')
print('='*20)
for i in range(0, len(alunos)):
    print(f'{i:<3} {alunos[i][0]:<10} {alunos[i][2]:<4}')
print('='*20)
while True:
    print()
    opc = int(input('De qual aluno gostaria de ver a nota? 999 para sair '))
    print()
    if opc >= len(alunos) and opc != 999:
        print('Aluno não encontrado...')
    elif opc != 999:
        print(f'As notas do aluno {alunos[opc][0].upper()} são: ')
        print()
        print('=' * 20)
        print(f'{"NOTA 1":<9}  {"NOTA 2":<9}')
        print(f'{alunos[opc][1][0]:<9}  {alunos[opc][1][1]:<9}')
        print('=' * 20)
    if opc == 999:
        break
