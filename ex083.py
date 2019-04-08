'''
Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

# testa se uma expressao matematica abre e fecha os parenteses de forma correta

expressao = list(input('Informe a expressão a ser analizada: '))
teste = False
posOpen = list()
posClose = list()
for i, j in (enumerate(expressao)):
    if j == '(':
        posOpen.append(i)
    elif j == ')':
        posClose.append(i)
if len(posOpen) == len(posClose):
    teste = True
    for i in range(0, len(posOpen)):
        if posOpen[i] > posClose[i]:
            teste = False
if teste:
    print('A expressão é VÁLIDA (parenteses)')
else:
    print('A expressão é INVÁLIDA (parenteses)')


'''
# guanabara
expr = str(input('Digite '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('OK')
else:
    print('NO!')
'''