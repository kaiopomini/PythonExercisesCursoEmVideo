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

