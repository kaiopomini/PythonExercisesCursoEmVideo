'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior
número no dado.'''

from random import randint
from operator import itemgetter
from time import sleep

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado D6')
    sleep(1)
print()
print(f'#### {"RANKING":^14} ####')
print(f'{"POSIÇÃO":<9}{"JOGADOR":<8} {"PONTOS":<2}')
for i, j in enumerate(ranking):
    sleep(1)
    print(f'{i+1:.<8} {j[0]:.<13} {j[1]:<2}')
print('#'*24)
