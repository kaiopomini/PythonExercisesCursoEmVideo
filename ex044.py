'''Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''

valor = float(input('Informe o valor do produto: '))
opc = int(input('''1 - Á VISTA (DINHEIRO)
2 - Á VISTA (CARTÃO)
3 - 2x 
4 - 3x ou mais
Informe a opção de pagamento conforme a tabela acima: '''))
if opc == 1:
    print('O valor do produto será R${:.2f}, ou seja 10% de desconto.'.format(valor-(valor*0.10)))
elif opc == 2:
    print('O valor do produto será R${:.2f}, ou seja 5% de desconto.'.format(valor-(valor*0.05)))
elif opc == 3:
    print('O valor do produto será R${:.2f}.'.format(valor))
elif opc == 4:
    print('O valor do produto será R${:.2f}, ou seja 20% de juros.'.format(valor+(valor*0.20)))
else:
    print('Opção inválida, tente novamente.')
