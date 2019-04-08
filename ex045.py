'''Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.'''

import random
opc = int(input('1 = PEDRA\n2 = PAPEL\n3 = TESOURA\nInforme sua escolha conforme as opções acima: '))
opcPc = random.randint(1,3)

'''
1 = pedra, 2 = papel, 3 = tesoura
'''
if opc == 1:
    print('você escolheu PEDRA')
    if opcPc == 1:
        print('O computador escolheu PEDRA')
        print('o resultado foi EMPATE.')
    elif opcPc == 2:
        print('O computador escolheu PAPEL')
        print('PEDRA perde para PAPEL, você PERDEU.')
    elif opcPc == 3:
        print('O computador escolheu TESOURA')
        print('PEDRA ganha de TESOURA, você VENCEU!!!\nPARABÉNS!!!!!!!!!!!!')
elif opc == 2:
    print('você escolheu PAPEL')
    if opcPc == 1:
        print('O computador escolheu PEDRA')
        print('PAPEL ganha de PEDRA, você VENCEU!!!\nPARABÉNS!!!!!!!!!!!!!!.')
    elif opcPc == 2:
        print('O computador escolheu PAPEL')
        print('o resultado foi EMPATE.')
    elif opcPc == 3:
        print('O computador escolheu TESOURA')
        print('PAPEL perde para TESOURA, você PERDEU.')
elif opc == 3:
    print('você escolheu TESOURA')
    if opcPc == 1:
        print('O computador escolheu PEDRA')
        print('TESOURA perde para PEDRA, você PERDEU')
    elif opcPc == 2:
        print('O computador escolheu PAPEL')
        print('TESOURA ganha de PAPEL, você VENCEU!!!\nPARABÉNS!!!!!!!!!!!! ')
    elif opcPc == 3:
        print('O computador escolheu TESOURA')
        print('o resultado foi EMPATE.')
else:
    print('Escolha inválida, tente novamente.')
