'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o
(com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime

trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
trabalhador['idade'] = datetime.now().year - int(input('Ano nascimento: '))
trabalhador['ctps'] = int(input('Informe sua CTPS ou 0 caso não tenha: '))
if trabalhador['ctps'] != 0:
    trabalhador['contratacao'] = int(input('Informe o ano de contratação: '))
    trabalhador['salario'] = float(input('Informe o salário:R$ '))
    trabalhador['aposentadoria'] = 35 - (datetime.now().year - trabalhador['contratacao']) + trabalhador['idade']
for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')
