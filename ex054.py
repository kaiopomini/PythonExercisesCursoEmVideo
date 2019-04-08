'''Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date
contadorMaioridade = 0
dataAtual = date.today()
for i in range(1, 8):
    anoNascimento = int(input('Informe a idade da pessoa numero {}: '.format(i)))
    if (dataAtual.year - anoNascimento) >= 18:
        contadorMaioridade += 1
print('Entre as 7 pessoas informada {} pessoas são MAIOR DE IDADE e {} são MENOR DE IDADE.'.format(contadorMaioridade, 7 - contadorMaioridade))
