'''Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

s = float(input('Informe o salário: '))
if s > 1250:
    print('Você tem direito a um acrécimo de 10%, seu novo salário será R${:.2f}'.format(s*1.1))
else:
    print('Você tem direito a um acrécimo de 15%, seu novo salário será R${:.2f}'.format(s*1.15))
