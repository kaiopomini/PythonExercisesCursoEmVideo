'''Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''

n1 = int(input('Informe um numero inteiro: '))
n2 = int(input('Informe outro numero inteiro: '))
if n1 > n2:
    print('{} é maior que {}!'.format(n1, n2))
elif n1 < n2:
    print('{} é menor que {}!'.format(n1, n2))
else:
    print('Os dois numeros são iguais!')
