'''
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome
do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo
isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

total = 0
jogador = dict()

gols = list()
jogador['nome'] = str(input('Informe o NOME do jogador: '))
partidas = int(input('Quantas partidas ele jogou? '))
for i in range(0, partidas):
    gols.append(int(input(f'Quantos gols foram feiros no jogo {i+1}? ')))
    total += gols[i]
jogador['gols'] = gols[:]
jogador['total'] = total
print('='*60)
print(jogador)
print('='*60)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('='*60)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas: ')
for i, j in enumerate(jogador['gols']):
    print(f'{"    => "}No jogo {i+1}, fez {j} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
