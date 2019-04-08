'''Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''

n = str(input('Informe um numero de 0 a 9999: '))
n = (4-len(n))*'0'+n
print('Unidade {}\nDezena {}\nCentena {}\nMilhar {}'.format(n[3], n[2], n[1], n[0]))


'''

modo com int (guanabara)

num = int(input('informe um nome de 0 a 9999: ))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade {}\nDezena {}\nCentena {}\nMilhar {}'.format(u, d, c, m))

'''
