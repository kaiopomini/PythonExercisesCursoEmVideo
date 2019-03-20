maiorPeso = 0
menorPeso = 0
for i in range(1, 6):
    peso = float(input('Informe o peso da pessoa {}: '.format(i)))
    if peso > maiorPeso:
        maiorPeso = peso
    else:
        menorPeso = peso
print('O MAIOR peso registrado foi de {:.3f}Kg e o MENOR peso registrado foi de {:.3f}Kg.'.format(maiorPeso, menorPeso))

