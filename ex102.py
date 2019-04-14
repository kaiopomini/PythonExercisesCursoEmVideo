'''Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não
na tela o processo de cálculo do fatorial.'''


def fatorial(n, show=False):
    """
    Funçao calcula o fatorial do numero passado por parametro e caso a show seja True mostra a conta feita.
    caso o numero informado seja negativo, retornará 0, o qual poderá ser utilizado para possivel mensagem de erro.
    :param n: valor a realizar fatorial
    :param show: mostra a operação efetuada
    :return: resultado fatorial, se o numero negativo retorta 0 (inválido)
    """
    r = 0
    if n < 0:
        if show:
            print(f'Não é possivel calcular fatorial de numero negativo')
        return 0
    elif n < 2:
        if show:
            print(f'O fatorial de {n} é: 1')
        return 1
    else:
        if show:
            print(f'O fatorial de {n} é: ', end='')
        for i in range(n, 0, -1):
            r += n*i
            if show:
                if i == 1:
                    print(f'{i} = ', end='')
                else:
                    print(f'{i} x ', end='')
        return r


print(fatorial(5))
print(fatorial(10, True))
print(fatorial(0))
print(fatorial(-1))
