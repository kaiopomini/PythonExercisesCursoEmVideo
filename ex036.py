'''Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o
 valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30%
 do salário ou então o empréstimo será negado.'''

vcasa = float(input('Informe o valor da CASA a ser adquiridas: '))
sal = float(input('Informe o valor do SALÁRIO do contratante: '))
tempoAnos = int(input('Informe o tempo em ANOS que o contrato será adimplido: '))
valorMensal = (vcasa / (tempoAnos*12))
print('O valor da prestação da casa é de R$ {:.2f}.'.format(valorMensal))
print('30% do salário é {:.2f}.'.format(sal*0.3))
if valorMensal <= sal*0.3:
    print('Você está apto a contratar, pois a parcela da casa não excede 30% do seu salário.')
else:
    print('Você não está apto a contratar, pois a parcela da casa excede 30% do seu salário.')
