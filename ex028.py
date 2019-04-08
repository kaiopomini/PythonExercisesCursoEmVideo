'''Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para
 o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
  venceu ou perdeu.'''

import random
print('Olá! Esse é um jogo de adivinhação!!')
ne = int(input('Informe um numero entre 0 e 5: '))
nr = random.randint(0, 5)
if ne == nr:
    print('Parabéns, você acertou, o número que eu pensei foi {}!!!'.format(nr))
else:
    print('Que pena, você errou, o número que eu pensei foi {}.'.format(nr))
print('-- FIM DE JOGO --')

'''
 com cores  e sleep
 
 
from random import randint
from time import sleep  # para o pc esperar
from termcolor import colored  # para dar cor as fontes
pc = randint(0, 5)
print(colored('-=-', 'yellow') * 19)
print(colored('Vou pensar em um número entre 0 e 5. Tente adivinhar...', 'blue'))
print(colored('-=-', 'yellow') * 19)
resp = int(input('Em que número eu pensei? '))
print(colored('PROCESSANDO...', 'magenta'))
sleep(2)
if resp == pc:
    print(colored('PARABÉNS! Você conseguiu me vencer!', 'green'))
else:
    print(colored('GANHEI! Eu pensei no {} e não no {}.', 'red').format(pc, resp))﻿



'''
