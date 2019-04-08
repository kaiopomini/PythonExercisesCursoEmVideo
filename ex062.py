'''Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

soma = int(input('Informe o PRIMEIRO TERMO da Progressão Aritimética: '))
razao = int(input('Informe a RAZÃO da Progressão Aritimética: '))
parada = 10
contador = 1
while parada != 0:
    for i in range(0, parada):
        print('a{} = {}'.format(contador, soma))
        soma += razao
        contador += 1
    parada = int(input('Quantos termos adcionais voce deseja? sendo "0" para sair: '))
print('Obrigado por usar a calculadora de PA Kaio Pomini!!')
