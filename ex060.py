'''
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''

contador = soma = fatorial = int(input('Informe um numero inteiro: '))
print('Fatorial com while\n')
print('{} ! = {}'.format(fatorial, fatorial), end=' x ')
while contador != 1:
    soma = soma * (contador-1)
    if contador != 2:
        print('{}'.format(contador-1), end=' x ')
    else:
        print('{}'.format(contador - 1), end=' = ')
    contador += -1
print('{}'.format(soma))
print('O Resultado de {}! é {} '.format(fatorial, soma))
print('\nFatorial com for!\n')
soma = fatorial
print('{} ! = {}'.format(fatorial, fatorial), end=' x ')
for i in range(fatorial-1, 0, -1):
    soma = soma * i
    if i != 1:
        print('{}'.format(i), end=' x ')
    else:
        print('{}'.format(i), end=' = ')
print('{}'.format(soma))
print('O Resultado de {}! é {} '.format(fatorial, soma))
