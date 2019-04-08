'''Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''

n = str(input('Informa uma frase qualquer: ').strip())
a = n.split()
n = ' '.join(a)
print('Aparecem {} vezes a letra "A" em sua frase, seja ela maiuscula ou minuscula.'.format(n.upper().count('A')))
print('Na primera vez aparece na posição {} e na segunda vez na posição {}'.format((n.upper().find('A'))+1, n.upper().rfind('A')+1))
