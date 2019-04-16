'''Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o
nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum
dado não tenha sido informado corretamente.'''


def ficha(a='<desconhecido>', b=0):
    print(f'O jogador {a} fez {b} gols no campeonato.')


a = str(input('Nome do jogador: '))
b = str(input('Numero de Gols: '))
if b.isnumeric():
    b = int(b)
else:
    g = 0
if a.strip() == '':
    ficha(b=b)
else:
    ficha(a, b)

