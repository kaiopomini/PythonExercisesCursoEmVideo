'''Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

# na epoca da resolução nao tinha camp. bras. ai foi usado o ingles

campeonatoIngles = ('Manchester City', 'Liverpool', 'Tottenham', 'Arsenal', 'Manchester United', 'Chelsea',
                    'Wolverhampton', 'Watford', 'West Ham', 'Leicester', 'Everton', 'Bournemouth', 'Newcastle',
                    'Crystal Palace', 'Brighton', 'Southampton', 'Burnley', 'Cardiff', 'Fulham', 'Huddersfield')

print(f'Os 5 primeiros colocados são: {campeonatoIngles[0:5]}')
print(f'Os 5 primeiros colocados são: {campeonatoIngles[19:15:-1]}')
print(f'Os times em ordem alfabetica são: {sorted(campeonatoIngles)}')
for i in range(0, len(campeonatoIngles)):
    if campeonatoIngles[i] == 'West Ham':
        print(f'O {campeonatoIngles[i]} está na posição {i}')
