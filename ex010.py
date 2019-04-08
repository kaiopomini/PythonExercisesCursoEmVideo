'''Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.'''

money = float(input('Enter how much money you have in your wallet in R$: '))
print('You can buy {:.2f}$!'.format(money/3.27))
