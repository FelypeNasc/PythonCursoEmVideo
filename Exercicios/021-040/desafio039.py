# crie um código que leia o ano de um jovem e
# Diga se ele ainda vai se alistar, já é a hora de se alistar ou se já passou da hora
import datetime
anoNasc = int(input('Digite seu ano de nascimento: '))
anoAtual = datetime.date.today().year
idade = anoAtual - anoNasc
tempoFalta = 18 - idade
anoAlist = anoAtual + tempoFalta


if idade < 18:
    print('Você ainda não precisa se alistar!')
    print(f'Ainda faltam {tempoFalta} anos que será em {anoAlist}')

elif idade == 18:
    print('Você deve se alistar imediatamente!')
    print(f'Nascidos no ano de {anoNasc} completam 18 anos neste ano.')

else:
    tempoFalta = idade - 18
    anoAlist = anoAtual - tempoFalta
    print(f'Você deveria ter se alistado há {tempoFalta} anos.')
    print(f'Seu alistamento foi em {anoAlist}!')
