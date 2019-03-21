numero = int(input('Informe um numero inteiro, sendo 999 para parar: '))
contador = soma = 0
while numero != 999:
    soma += numero
    contador += 1
    numero = int(input('Informe um numero inteiro, sendo 999 para parar: '))
print('Foram digitados {} e a soma deles é {}'.format(contador, soma))