'''Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''

vel = int(input('Informe a velocidade do carro em KM/H: '))
if vel > 80:
    print('''Você foi multado pois estava em {}KM/H
A multa é de R$7.00 por KM/h acima de 80KM/H
Portanto, sua multa é no valor de R${:.2f}.'''.format(vel, (vel - 80)*7))
else:
    print('Continue assim! você está no limite de velocidade!')
