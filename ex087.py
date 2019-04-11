'''
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

somaPar = somaC3 = maiorS = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Informe o numero da posição [{l+1}],[{c+1}]: '))
print('=-'*20)
maiorS = matriz[1][0]  # atribui o valor da posição 1,0 para comparar se os demais são maiores
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')  # Print a tabela
        if matriz[l][c] % 2 == 0:  # identifica os numeros pares
            somaPar += matriz[l][c]
        if c == 2:  # identifica a coluna 3
            somaC3 += matriz[l][c]
        if l == 1 and matriz[l][c] > maiorS:  # identifica a linha 2 e testa se a posição da matriz é maior que a var maiorS
            maiorS = matriz[l][c]
    print()
print('=-'*20)
print(f'Soma da coluna 3 é {somaC3}')
print(f'Soma dos numeros pares é {somaPar}')
print(f'O maior valor da segunda linha é {maiorS}')
