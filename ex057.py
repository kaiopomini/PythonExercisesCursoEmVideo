'''Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso
esteja errado, peça a digitação novamente até ter um valor correto.'''

sexo = 'a'
while (sexo != 'F') and (sexo != 'M'):
    sexo = str(input('Informe seu sexo, sendo M para Masculino e F para Feminindo: ').strip().upper())
    if (sexo != 'F') and (sexo != 'M'):
        print('"{}" NÃO É UMA OPC VÁLIDA!'.format(sexo))
if sexo == 'M':
    print('Você é do sexo Masculino')
else:
    print('Você é do sexo FEMININO')
