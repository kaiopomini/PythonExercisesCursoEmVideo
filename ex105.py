'''Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)'''


def notas(* n, sit=False):
    """
    Função que analiza as notas e retorna na forma de dicionário as informações: TOTAL(quantidade de notas),
    MAIOR(maior nota), MENOR(menor nota), MEDIA(media simples das notas) e opcionalmente a SITUAÇÃO(conforme a média,
    sendo: RUIM menor ou igual a 6, BOM menor ou igual a 8 e ÓTIMO acima de 8.
    :param n: Valores das notas float or int
    :param sit: opcional - Boolean
    :return: dicionário contendo os campos total, maior, menor, media, situação(opcional).
    """
    soma = 0
    maior = menor = n[0]
    for i in range(0, len(n)):
        soma += n[i]
        if n[i] > maior:
            maior = n[i]
        if n[i] < menor:
            menor = n[i]
    nota = {'total': len(n),
            'maior': maior,
            'menor': menor,
            'media': soma/(len(n))
            }
    if sit:
        if nota['media'] <= 6:
            nota['situação'] = 'RUIM'
        elif nota['media'] <= 8:
            nota['situação'] = 'BOM'
        else:
            nota['situação'] = 'ÓTIMO'
    return nota


a = notas(5, 4, 4, sit=True)
b = notas(8, 9, 7, sit=True)
c = notas(8, 8, 10)
d = notas(8, 8, 10, sit=True)

print(a)
print(b)
print(c)
print(d)
