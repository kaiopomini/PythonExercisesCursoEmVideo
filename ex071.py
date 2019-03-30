print('=' * 30)
print(f'{"BANCO CEV":^30}')
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

'''
#resolução 1

saque = aux = int(input('Informe o valor a ser sacado: '))
cont50 = cont20 = cont10 = cont1 = 0



if aux >= 50:
    auxAnterior = aux
    aux = aux % 50
    cont50 = auxAnterior // 50

if aux >= 20:
    auxAnterior = aux
    aux = aux % 20
    cont20 = auxAnterior // 20

if aux >= 10:
    auxAnterior = aux
    aux = aux % 10
    cont10 = auxAnterior // 10

if aux >= 1:
    auxAnterior = aux
    aux = aux % 1
    cont1 = auxAnterior // 1

if cont50 > 0:
    print(f'{cont50} notas de R$50.00')
if cont20 > 0:
    print(f'{cont20} notas de R$20.00')
if cont10 > 0:
    print(f'{cont10} notas de R$10.00')
if cont1 > 0:
    print(f'{cont1} notas de R$1.00')
    
'''