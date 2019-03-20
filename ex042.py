a = float(input('Informe o valor da primeira reta: '))
b = float(input('Informe o valor da segunda reta: '))
c = float(input('Informe o valor da terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print('Essas retas formam um triangulo EQUILÁTERO')
    elif (a == b) or (b == c) or (a == c):
        print('Essas retas formam um triangulo ISÓCELES')
    else:
        print('Essas retas formam um triangulo ESCALENO')
else:
    print('Essas retas não formam um triangulo.')
