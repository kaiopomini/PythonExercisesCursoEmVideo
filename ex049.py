'''Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora
utilizando um laço for.'''

n1 = int(input('enter with the integer number: '))
print('The multiplication table of {} is'.format(n1))
for i in range(0, 11):
    print('{} x {} = {}'.format(n1, i, n1*i))
