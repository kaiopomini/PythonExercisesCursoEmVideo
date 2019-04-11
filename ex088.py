'''
Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''

from random import randint

megasena = []
aux = []
num = numRepetidos = 0
jogosRepetidos = []
print('+'*40)
print(f'{"SORTEADOR DA SORTE!!!":^40}')
print('+'*40, '\n')
qJogos = int(input('Quantos jogos você quer? '))
print('')
for i in range(0, qJogos):
    while True:
        for j in range(0, 6):
            while True:
                num = randint(1, 60)
                if num not in aux:
                    break
                else:
                    numRepetidos += 1  # Teste de funcionamento
            aux.append(num)
        aux.sort()
        if aux not in megasena:
            break
        else:
            jogosRepetidos.append(aux[:])  # Teste de funionamento

    megasena.append(aux[:])
    aux.clear()
megasena.sort()
print('+'*40, '\n')
print('Os jogos sorteados foram: \n')
for i, j in enumerate(megasena):
    print(f'Jogo {i+1}: {j}')

'''
# TESTE algoritimo
 
jogosRepetidos.sort()
print(f'Numeros repetidos {numRepetidos}')
print(f'jogos repetidos {len(jogosRepetidos)}')
for i in jogosRepetidos:
    print(i)
'''