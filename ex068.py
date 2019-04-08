'''Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. '''

from random import randint
contadorVitorias = 0
print('VAMOS JOGAR PAR OU IMPAR!\n')
while True:
    jogador = int(input('Informe um numero '))
    while True:
        parImpar = str(input('Escolha entre PAR OU IMPAR: P/I ').strip().upper())
        if parImpar == 'P':
            break
        elif parImpar == 'I':
            break
    pc = randint(0, 9)
    resultado = (pc+jogador) % 2
    print('\n')
    if resultado == 0:
        print(f'Você escolheu {jogador} e o computador escolheu {pc}, totalizando {jogador+pc} que é PAR')
        if parImpar == 'P':
            print('Você escolheu PAR, você ganhou!')
            contadorVitorias += 1
        elif parImpar == 'I':
            print('Você escolheu IMPAR, você perdeu!')
            break
    else:
        print(f'Você escolheu {jogador} e o computador escolheu {pc}, totalizando {jogador + pc} que é IMPAR')
        if parImpar == 'I':
            print('Você escolheu IMPAR, você ganhou!')
            contadorVitorias += 1
        elif parImpar == 'P':
            print('Você escolheu PAR, você perdeu!')
            break
    print('\n')
print(f'\nGAME OVER!! Sua quantidade de vitórias foi {contadorVitorias}')
