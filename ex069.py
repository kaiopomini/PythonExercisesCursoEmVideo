contador18 = contadorHomens = contadorMulheres20 = 0
while True:
    idade = int(input('Informe sua idade: '))
    while True:
        sexo = str(input('Informe seu sexo, sendo M para MASCULINO e F para Feminino: M/F ').strip().upper())
        if sexo == 'M':
            break
        elif sexo == 'F':
            break
    if sexo == 'M':
        contadorHomens += 1
    elif idade < 20:
        contadorMulheres20 += 1
    if idade > 18:
        contador18 += 1
    while True:
        continua = str(input('Deseja continuar cadastrando? S/N ').strip().upper())
        if continua == 'N':
            break
        elif continua == 'S':
            break
    if continua == 'N':
        break
print(f'\nForam cadastrados:\n{contador18} pessoa(s) com mais de 18 anos;\n{contadorHomens} Homen(s); e\n{contadorMulheres20} Mulher(es) com menos de 20 Anos.')

