# Ordenador de vetor

vetor = list()


def ordenar(lst):
    """
    função organiza uma lista de numeros e escreve na tela ele organizado em ordem crescente.
    :param lst: lista
    :return: não há retorno
    """

    for i in range(0, len(lst)-1):
        for j in range(0, len(lst)-(i+1)):
            if lst[j] > lst[j+1]:
                aux = lst[j+1]
                lst[j+1] = lst[j]
                lst[j] = aux
            print(lst, j, i)  # for test
    print(lst)


while True:
    num = float(input('Informe um numero (999 para SAIR): '))
    if num == 999:
        break
    else:
        vetor.append(num)
print(vetor)

ordenar(vetor)
