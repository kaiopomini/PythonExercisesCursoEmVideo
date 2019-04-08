'''Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na
sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

listagem = ('Carne Kg', 11.25, 'Leite', 5.50, 'Arroz', 10.90, 'Cachorro', 199.90, 'Biscoito Recheado', 12.90, 'Uva', 8)
print('='*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('='*40)
for i in range(0, len(listagem)):
    if i % 2 == 0:
        print(f'{listagem[i]:.<30}', end='')
    else:
        print(f'R$ {listagem[i]:>7.2f}')
print('='*40)
print(f'{"TENHA UM BOM DIA!":^40}')
