
num = int(input('Informe um numero inteiro: '))
opc = int(input('''Informe a opção de qual base você gostaria de converter, sendo:
 1 = Binário; 
 2 = Octal; e 
 3 = Hexadecimal.'''))
if opc == 1:
    print('o numero {} em binário é {}'.format(num, bin(num)[2:]))
elif opc == 2:
    print('o numero {} em octal é {}'.format(num, oct(num)[2:]))
elif opc == 3:
    print('o numero {} em hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('a opção escolhida é inválida, por favor, tente novamente.')
