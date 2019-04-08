'''Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os
 espaços.'''

frase = input('Informe uma frase: ')
fraseSemEspaço = frase.upper().split()
fraseSemEspaço =''.join(fraseSemEspaço)
fraseContraria = ''

for i in range(len(fraseSemEspaço), 0, -1):
    fraseContraria += fraseSemEspaço[i-1]
print('O inverso de {} é {}.'.format(fraseSemEspaço, fraseContraria))
if fraseSemEspaço == fraseContraria:
    print('A frase "{}" é um polídromo'.format(frase))
else:
    print('A frase"{}" não é um polídromo'.format(frase))
