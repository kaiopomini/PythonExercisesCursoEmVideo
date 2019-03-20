mulheresSub20 = 0
mediaDeIdade = 0
idadeHomemMaisVelho = 0
nomeHomemMaisVelho = ''
for i in range(1, 5):
    nome = str(input('Informe o Nome da pessoa {}: '.format(i)).strip())
    idade = int(input('Agora informe a idade em anos: '))
    sexo = str(input('Informe tambem o sexo, sendo: F para Feminino e M para Masculino: ').upper())
    mediaDeIdade += idade
    if sexo == 'M':
        if idade > idadeHomemMaisVelho:
            idadeHomemMaisVelho = idade
            nomeHomemMaisVelho = nome
    else:
        if idade < 20:
            mulheresSub20 += 1
mediaDeIdade = mediaDeIdade/4
print('A média de idade do grupo é de {} anos.'.format(mediaDeIdade))
if nomeHomemMaisVelho != '':
    print('O nome do homem mais velho do grupo é {}.'.format(nomeHomemMaisVelho))
print('E {} mulher(es) tem menos que 20 Anos.'.format(mulheresSub20))
