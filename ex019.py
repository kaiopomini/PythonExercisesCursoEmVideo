import random
a1 = str(input('Informe o nome do primeiro aluno: '))
a2 = str(input('Informe o nome do segundo aluno: '))
a3 = str(input('Informe o nome do terceiro aluno: '))
a4 = str(input('Informe o nome do quarto aluno: '))
print('O aluno sorteado para apagar o quadro foi {}.'.format(random.choice([a1, a2, a3, a4])))

'''
é possível usar lista: 

lista = [a1, a2, a3, a4]
'''