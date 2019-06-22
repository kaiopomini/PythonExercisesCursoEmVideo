from random import randrange


def geradordevetor(a):
    vetor = list()
    for i in range(0, a):
        vetor.append(randrange(0, 999))
    return vetor


vetor = geradordevetor(3)
contador = aux = 0
tamanho = len(vetor)
print(vetor)
while contador < (len(vetor) - contador):

    for i in range(contador, (tamanho-contador-1)):

        if vetor[i] > vetor[i+1]:
            aux = vetor[i+1]
            vetor[i+1] = vetor[i]
            vetor[i] = aux

    for j in range((tamanho-contador-2), contador, -1):

        if vetor[j] < vetor[j-1]:
            aux = vetor[j - 1]
            vetor[j - 1] = vetor[j]
            vetor[j] = aux
    contador += 1

print(vetor)
vetor.sort()
print(vetor)