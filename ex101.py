'''Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO
nas eleições.'''


def voto(a):
    """
    A função recebe o ano de nascimento, compara com o ano atual e retorna uma string com informaçoes sobre a situação
    de voto em relação a idade (years)
    :param a: Ano de nascimento
    :return: SEM RETORNO
    """
    from datetime import datetime
    b = datetime.now().year - a
    if b < 16:
        return f'Com {b} anos: VOTO NEGADO'
    elif b < 18:
        return f'Com {b} anos: VOTO OPCIONAL'
    elif b < 65:
        return f'Com {b} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {b} anos: VOTO OPCIONAL'


print(voto(int(input('Em que ano você nasceu? '))))
