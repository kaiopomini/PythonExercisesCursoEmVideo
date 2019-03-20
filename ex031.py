n = float(input('Informa a distancia de sua viagem: '))
if n <= 200:
    print('O valor de sua viagem é R${:.2f}, ou seja, R$0,50 por KM em viagem até 200km.'.format(n*0.5))
else:
    print('O valor de sua viagem é R${:.2f}, ou seja, R$0,45 por KM em viagens acima de 200km'.format(n*0.45))
