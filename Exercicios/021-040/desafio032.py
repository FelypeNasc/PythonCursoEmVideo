#crie um código que leia um ano e diga se ele é bissexto ou não
from datetime import date
ano = int(input('Qual ano você deseja analisar? (Digite 0 para o ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano bissexto!'.format(ano))
else:
    print('{} não é um ano bissexto!'.format(ano))
