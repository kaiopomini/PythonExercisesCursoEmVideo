campeonatoIngles = ('Manchester City', 'Liverpool', 'Tottenham', 'Arsenal', 'Manchester United', 'Chelsea',
                    'Wolverhampton', 'Watford', 'West Ham', 'Leicester', 'Everton', 'Bournemouth', 'Newcastle',
                    'Crystal Palace', 'Brighton', 'Southampton', 'Burnley', 'Cardiff', 'Fulham', 'Huddersfield')

print(f'Os 5 primeiros colocados são: {campeonatoIngles[0:5]}')
print(f'Os 5 primeiros colocados são: {campeonatoIngles[19:15:-1]}')
print(f'Os times em ordem alfabetica são: {sorted(campeonatoIngles)}')
for i in range(0, len(campeonatoIngles)):
    if campeonatoIngles[i] == 'West Ham':
        print(f'O {campeonatoIngles[i]} está na posição {i}')