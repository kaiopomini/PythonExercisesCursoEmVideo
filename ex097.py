'''
Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como
parâmetro e mostre uma mensagem com tamanho adaptável.
'''


def escreva(frase):
    print('~'*(len(frase)+2))
    print(f' {frase} ')
    print('~'*(len(frase)+2))


escreva('Kaio')
escreva('teste de funcionamento')
escreva('a')
