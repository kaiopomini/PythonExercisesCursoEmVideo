'''Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função
input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')'''


def leiaInt(a):
    """
    função recebe qualquer valor e verifica se é um valor decimal, caso não seja ele solicita que digita novamente
    ficando nesse looping até que seja digitado um valor numerico decimal inteiro, retornando-o na forma de(int).
    :param a: qualquer valor
    :return: valor inteiro (int)
    """
    a = str(a)
    while not a.isdecimal():
        a = str(input('ERRO! informe um numero inteiro: '))
    a = int(a)
    return a


n = leiaInt(input('Informe um numero inteiro: '))
print(n)
