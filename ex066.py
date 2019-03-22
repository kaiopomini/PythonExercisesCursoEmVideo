contador = soma = 0
while True:
    numero = int(input('Informe um numero inteiro, ou "999" para sair: '))
    if numero == 999:
        break
    contador += 1
    soma += numero
print(f'Foram lidos {contador} número(s) que somados resultam em {soma}')