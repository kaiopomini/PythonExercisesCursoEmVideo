'''Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de
zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

while True:
    numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
               'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
    while True:
        opc = int(input('Informa um numero de 0 a 20: '))
        if 0 <= opc <= 20:
            print('Tente novamente! ', end='')
            break
    print(f'Você escolheu o numero {numeros[opc]}')
    while True:
        continuar = str(input('Gostaria de continuar? [S/N] ').strip().upper())
        if continuar == 'S' or continuar == 'N':
            break
    if continuar == 'N':
        break
