numero1 = float(input('Informe o numero 1: '))
numero2 = float(input('Informe o numero 2: '))
opc = -1
while opc != 5:
    print('os numeros que você escolheu foram:')
    print('Numero 1 = {}\nNumero 2 = {}'.format(numero1, numero2))
    print('[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] INFORMAR NOVOS NÚMEROS\n[5] SAIR')
    opc = int(input('informe uma das opções acima: ').strip())
    print('')
    if opc == 1:
        print('A soma de {} e {} é {}'.format(numero1, numero2, numero1+numero2))
    elif opc == 2:
        print('A multiplicação entre {} e {} é {}'.format(numero1, numero2, numero1*numero2))
    elif opc == 3:
        if numero1 > numero2:
            print('O número {} é MAIOR que {}'.format(numero1, numero2))
        elif numero1 < numero2:
            print('O número {} é MAIOR que {}'.format(numero2, numero1))
        else:
            print('O número {} é IGUAL a {}'.format(numero1, numero2))
    elif opc == 4:
        numero1 = float(input('Informe o numero 1: '))
        numero2 = float(input('Informe o numero 2: '))
    print('')
print('Obrigado por usar a calculadora pomini!')
