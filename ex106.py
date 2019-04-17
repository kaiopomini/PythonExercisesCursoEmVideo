from time import sleep
from random import randint


def cor(a=True):
    """
    Gera uma cor aleatoria e retorna seu codigo, sendo que se a=False, nao mostra cor
    :param a:True/False
    :return: cod collor
    """
    fundo = randint(41, 48)
    letra = 30  # preferi não randomizar
    if a:
        cor = f'\033[1;{letra};{fundo}m'
    else:
        cor = f'\033[0;0;0m'
    return cor


def ajuda(a):
    """
    funciona junto com a fução cor(), ou seja, depende dela, pois mostra a função help COLORIDA
    :param a: qualquer parametro
    :return: escreve na tela / sem retorno
    """
    print(f'{cor()}', end='')
    sleep(2)
    print('=' * 50)
    print('PROCESSANDO...')
    print('=' * 50)
    sleep(2)
    print(f'{cor()}', end='')
    print(f'{cor()}{help(a)}', end='')
    print(f'{cor(a=False)}')


print(f'{cor()}', end='')
print('='*50)
print('SISTEMA DE AJUDA PyHELP')
print('='*50)
print(f'{cor(a=False)}', end='')
while True:
    a = str(input(f'Função ou Biblioteca > '))
    if a.strip().upper() == 'FIM':
        print(f'{cor()}', end='')
        print('=' * 50)
        print('OBRIGADO POR USAR O SISTEMA PyHELP')
        print('=' * 50)
        break
    ajuda(a)
