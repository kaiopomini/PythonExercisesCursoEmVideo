'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
visualização de detalhes do aproveitamento de cada jogador.'''

time = list()
jogador = dict()
gols = list()

while True:
    total = 0
    jogador['nome'] = str(input('Informe o NOME do jogador: '))
    partidas = int(input('Quantas partidas ele jogou? '))
    for i in range(0, partidas):
        gols.append(int(input(f'Quantos gols foram feiros no jogo {i+1}? ')))
        total += gols[i]
    jogador['gols'] = gols[:]
    gols.clear()
    jogador['total'] = total
    time.append(jogador.copy())
    while True:
        opc = str(input('Deseja continuar? [S/N] ')).upper()
        if opc == 'S' or opc == 'N':
            break
        else:
            print('Opção inválida, informe S ou N.')
    if opc == 'N':
        break
print('='*64)

print(f'{"COD":<4}{"NOME":<15}{"GOLS":<40}{"TOTAL":<3}')
print('-'*64)
for i, j in enumerate(time):
    print(f' {i:<2} {j["nome"]:<14} {str(j["gols"]):<39}  {str(j["total"]):<4}')
print('-'*64)
print()
while True:
    opc2 = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    print()
    if opc2 == 999:
        break
    else:
        if 0 <= opc2 < len(time):

            print(f'-- Levantamento do jogador {time[opc2]["nome"]}')
            for i in range(0, len(time[opc2]["gols"])):
                print(f'     No jogo {i} fez {time[opc2]["gols"][i]} gols')
            print()
        else:
            print('Erro! Jogador não encontrado. Tente novamente...')
            print()
print('='*64)
