from datetime import date
nascimento = int(input('Informe o ano que voce nasceu: '))
dataAtual = date.today()
if (dataAtual.year - nascimento) < 18:
    print('Você ainda vai se alistar em {} ano(s) no serviço militar, em {}, ano em que completa 18 anos.'.format(18-(dataAtual.year-nascimento), nascimento+18))
elif (dataAtual.year - nascimento) == 18:
    print('Você está apto para se alistar no serviço militar pois já tem 18 anos.')
else:
    print('Você está {} ano(s) atrazado para o alistamento, regularize-se já!'.format((dataAtual.year-nascimento)-18))
