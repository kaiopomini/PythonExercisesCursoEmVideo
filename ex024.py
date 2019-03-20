n = str(input('Informe o nome da sua cidade: '))
nsplit = n.strip().split()
print('Sua cidade começa com "santo"? {}'.format('SANTO' in nsplit[0].upper()))
