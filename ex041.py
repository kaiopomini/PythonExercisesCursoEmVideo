'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''

from datetime import date
anoNascimentoAtleta = int(input('Informe o ano que você nasceu: '))
condicaoCategoriaNatacao = date.today().year - anoNascimentoAtleta
print('Sua idade é {} anos'.format(condicaoCategoriaNatacao))
if condicaoCategoriaNatacao <= 9:
    print('Sua categoria é MINIRM')
elif condicaoCategoriaNatacao <= 14:
    print('Sua categoria é INFANTIL')
elif condicaoCategoriaNatacao <= 19:
    print('Sua categoria é JUNIOR')
elif condicaoCategoriaNatacao <= 25:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')
