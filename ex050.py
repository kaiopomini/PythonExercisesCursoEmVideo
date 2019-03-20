soma = 0
for i in range(0, 6):
    numeroLido = int(input('Informe um numero: '))
    if (numeroLido % 2) == 0:
        soma += numeroLido
print('A soma dos números pares informados é de {}'.format(soma))
