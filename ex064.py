'''Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi
a soma entre eles (desconsiderando o flag).'''

numero = int(input('Informe um numero inteiro, sendo 999 para parar: '))
contador = soma = 0
while numero != 999:
    soma += numero
    contador += 1
    numero = int(input('Informe um numero inteiro, sendo 999 para parar: '))
print('Foram digitados {} e a soma deles é {}'.format(contador, soma))
