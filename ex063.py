n = int(input('informe a quantidade da sequencia fibonaci: '))
contador = a = b = 0
r = 1

while contador < n:
    if contador != (n-1):
        print(r, end=', ')
    else:
        print(r)
    b = a
    a = r
    r = a + b
    contador += 1
