n = int(input('Informe um ANO: '))
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('{} é Bissexto!'.format(n))


'''

resolução guanabara

from datetime inport date
n = int(input('Informe um ANO, sendo 0 para o ano atual '))
if n == date.today().year
    n = date.today().year
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('{} é Bissexto!'.format(n))
else:
    print('{} não é Bissexto!'.format(n))


'''