n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1+n2)/2
if media < 5:
    print('Sua média foi {:.2f} então você está REPROVADO.'.format(media))
elif media < 7:
    print('Sua média foi {:.2f} então você está de RECUPERAÇÃO.'.format(media))
else:
    print('Sua média foi {:.2f} então você está APROVADO.'.format(media))