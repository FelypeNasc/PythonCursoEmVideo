tabela = ('Fortaleza', 'Athletico-PR', 'Atlético-MG', 'Flamengo', 'Atlético-GO', 'Bragantino', 'Fluminense', 'Bahia', 'Palmeiras',
    'Corinthians', 'Ceará SC', 'Santos', 'São Paulo', 'Internacional', 'Juventude', 'Cuiabá', 'Sport Recife', 'Chapecoense', 'Grêmio', 'América-MG')
print ('''-------- BRASILEIRÃO 2021 -------

Os 5 primeiros colocados do campeonato: ''')

for time in range (0, 4):
    print (f'• {time+1} - {tabela[time]}')
input ()

print ('Os 5 últimos colocados do campeonato: ')
for time in range (15, 20):
    print(f'• {time+1} - {tabela[time]}')
input ()

print ('Times em ordem alfabética: ')

tabelaOrd = sorted(tabela)
for time in tabelaOrd:
    print (f'• {time}')
input ()

print (f'O Chapecoense está em {tabela.index("Chapecoense")}º lugar')
