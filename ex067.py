while True:
    numero = int(input('informe um numero, sendo negativo para sair: '))
    if numero < 0:
        break
    print(f'\nTABUADA DO {numero}\n')
    for i in range(0, 10):
        print(f'{numero} x {i+1} = {numero*(i+1)}')
    print('\n')
print('Obrigado por usar a Tabuada 2.0')