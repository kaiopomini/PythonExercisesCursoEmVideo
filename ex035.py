a = float(input('Informe o valor da primeira reta: '))
b = float(input('Informe o valor da segunda reta: '))
c = float(input('Informe o valor da terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    print('Essas retas podem formar um triangulo')
else:
    print('Essas retas não formam um triangulo.')

'''
1.0

from math import fabs
a = float(input('Informe o valor da primeira reta: '))
b = float(input('Informe o valor da segunda reta: '))
c = float(input('Informe o valor da terceira reta: '))
if fabs(b-c) < a:
    if a < b + c:
        if fabs(a-c) < b:
            if b < a + c:
                if fabs(a-b) < c:
                    if c < a + b:
                        print('Essas retas podem formar um triangulo')
else:
    print('Essas retas não formam um triangulo.')
'''