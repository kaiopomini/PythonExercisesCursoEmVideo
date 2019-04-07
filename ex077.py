# 2.0 version
palavras = ('paz', 'jix', 'league', 'teste', 'Som', 'paçoca', 'agua', 'suco', 'sfx')
for i in palavras:
    print(f'\nNa palavra {i.upper()} temos:', end=' ')
    for n in i:
        if n.lower() in 'aeiou':
            print(n, end=' ')

"""
# 1.0 version

palavras = ('paz', 'jix', 'league', 'teste', 'som', 'paçoca', 'agua', 'suco', 'sfx')
teste = False
for i in range(0, len(palavras)):
    print(f'Temos na palavra {(palavras[i])}', end='')
    for n in range(0, len(palavras[i])):
        if palavras[i][n] == 'a' or palavras[i][n] == 'e' or palavras[i][n] == 'i' or palavras[i][n] == 'o' or palavras[i][n] == 'u':
             print(f' {palavras[i][n]}', end='')
             teste = True
    if teste:
            print('.')
    else:
            print(' nenhuma vogal.')

    teste = False
"""
