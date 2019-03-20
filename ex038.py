n1 = int(input('Informe um numero inteiro: '))
n2 = int(input('Informe outro numero inteiro: '))
if n1 > n2:
    print('{} é maior que {}!'.format(n1, n2))
elif n1 < n2:
    print('{} é menor que {}!'.format(n1, n2))
else:
    print('Os dois numeros são iguais!')
