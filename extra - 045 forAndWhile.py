'''Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao
 aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a
 nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro
 aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.


Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova
antes dos alunos usarem o programa.
'''

senha = 'PROFADMIN'
gabarito = 'ABCDEABCDE'
contadorGabarito = 10
alunos = 0
media = 0
maior = 0
menor = 0

usuario = str(input('Informe o usuário "professor" para cadastrar o gabarito, ou qualquer outro para continuar: ').strip().upper())
if usuario == 'PROFESSOR':
    senhaInformada = str(input('Informe a senha de professor: ').strip().upper())
    while (senhaInformada != senha) and (senhaInformada != 'SAIR'):
        senhaInformada = str(input('SENHA INCORRETA! tente novamente ou digite SAIR para continuar no modo aluno: ').strip().upper())
    if senha == senhaInformada:
        gabarito = ''
        contadorGabarito = 0
        while senhaInformada != 'N':
            opc = str(input('informe a Resposta da questão {}: '.format(contadorGabarito+1)).strip().upper())
            gabarito += opc
            contadorGabarito += 1
            senhaInformada = str(input('Desejá continuar cadastrando? S/N: ').strip().upper())
        print('\n\n\n\n\n\n\n\n')

senhaInformada = ''
menor = contadorGabarito
print('MODO ALUNO\n')
while senhaInformada != 'N':
    nota = 0
    acertos = 0
    for i in range(0, contadorGabarito):
        opc = str(input('informe a Resposta da questão {}: '.format(i + 1)).strip().upper())
        if gabarito[i] == opc:
            acertos += 1
    if acertos > maior:
        maior = acertos
    if acertos < menor:
        menor = acertos

    nota = (10*acertos)/contadorGabarito
    media += nota
    alunos += 1
    senhaInformada = str(input('Desejá continuar cadastrando? S/N: ').strip().upper())
print('\n\nA MAIOR quantidade de acertos foram {} de {} perguntas'.format(maior, contadorGabarito))
print('A MENOR quantidade de acertos foram {} de {} perguntas'.format(menor, contadorGabarito))
print('O total de alunos que utilizaram o sistema foi de {}'.format(alunos))
print('A média da turma foi de {:.1f}'.format(media/alunos))


