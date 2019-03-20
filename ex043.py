peso = float(input('Informe seu peso em KILOGRAMAS: '))
altura = float(input('Informe sua altura em METROS: '))
imc = peso/(altura*altura)
if imc < 18.5:
    print('seu IMC é de {:.2f} e se encontra ABAIXO DO PESO .'.format(imc))
elif imc < 25:
    print('seu IMC é de {:.2f} e se encontra com PESO IDEAL.'.format(imc))
elif imc < 30:
    print('seu IMC é de {:.2f} e se encontra com SOBREPESO .'.format(imc))
elif imc < 40:
    print('seu IMC é de {:.2f} e se encontra com OBESIDADE .'.format(imc))
else:
    print('seu IMC é de {:.2f} e se encontra com OBESIDADE MÓRBIDA .'.format(imc))
