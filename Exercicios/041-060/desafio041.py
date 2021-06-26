# crie um código que leia a data de nascimento de uma pessoa e diga sua categoria:
# até 9 anos = mirim. até 14 anos: infantil, até 19 anos: junior. Até 20 Sênior, acima master.
print('-=-' *13)
print('       CONFEDERAÇÃO DE NATAÇÃO')
print('-=-' *13)
import datetime
anoNasc = int(input('Digite o ano de seu nascimento: '))
idade = (datetime.date.today().year) - anoNasc

if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JÚNIOR')
elif idade <= 20:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')

