'''
Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que
agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''

from random import randint
from time import sleep  # para o pc esperar
from termcolor import colored  # para dar cor as fontes -baixar cmd 'pip install termcolor'
pc = randint(0, 10)
print(colored('-=-', 'yellow') * 19)
print(colored('Vou pensar em um número entre 0 e 10. Tente adivinhar...', 'blue'))
print(colored('-=-', 'yellow') * 19)
resp = -1
contadorTentativas = 0
while resp != pc:
    resp = int(input('Em que número eu pensei? '))
    print(colored('PROCESSANDO...', 'magenta'))
    contadorTentativas += 1
    sleep(0.5)
    if resp == pc:
        print(colored('PARABÉNS! Você conseguiu me vencer, o número era {}, mas você gastou {} tentativa(s)!', 'green').format(pc, contadorTentativas))
    else:
        print(colored('HMMMM... Não é esse número, tente novamente!', 'red'))
