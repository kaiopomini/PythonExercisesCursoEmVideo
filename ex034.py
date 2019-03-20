s = float(input('Informe o salário: '))
if s > 1250:
    print('Você tem direito a um acrécimo de 10%, seu novo salário será R${:.2f}'.format(s*1.1))
else:
    print('Você tem direito a um acrécimo de 15%, seu novo salário será R${:.2f}'.format(s*1.15))
