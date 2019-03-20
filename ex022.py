nome = str(input('How is your full name? '))
nomesplit = nome.split()

print(' '.join(nomesplit).upper())
print(' '.join(nomesplit).lower())
print((len(' '.join(nomesplit)))-(' '.join(nomesplit).count(' ')))  # conta letras excluindo espaços
print(len(nomesplit[0].strip()))  # Conta letras primeiro nome

'''

uma solução mais facil é usar len(nomesplit), pois ele dá o resultado direto sem os espaços, reduzindo o consumo mem.
deixei as variaveis, mas é possivel remover a "nomecerto", no caso, sendo utilizado em seu lugar "' '.join(nomesplit)"

** nomecerto = ' '.join(nomesplit)  # arruma o nome com os espaços certos
essa função corrige os espaços informados pelo usuario, já implementado as informaçoes acima.

'''