maior = menor = numero = int(input('Informe um numero: '))
opc = 'S'
media = contador = 0
while opc != 'N':
    media += numero
    contador += 1
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    opc = str(input('Voce deseja continuar? S/N ').strip().upper())
    if (opc != 'S') and (opc != 'N'):
        while (opc != 'S') and (opc != 'N'):
            opc = str(input('Opção inválida! Responda S para continuar e N para sair. S/N ').strip().upper())
    elif opc == 'S':
        numero = int(input('Informe um numero: '))
media = media / contador
print('A média entre todos os valores foi {:.2f}'.format(media))
print('O maior numero foi {} e o menor numero foi {}'.format(maior, menor))
