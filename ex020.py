import random
a1 = str(input('Informe o nome do primeiro aluno: '))
a2 = str(input('Informe o nome do segundo aluno: '))
a3 = str(input('Informe o nome do terceiro aluno: '))
a4 = str(input('Informe o nome do quarto aluno: '))
print('A ordem de apresentação do trabalho será {}'.format(random.sample([a1, a2, a3, a4], k=4)))

'''
como foi feito com shuffle
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('a ordem será:')
print('lista')
'''