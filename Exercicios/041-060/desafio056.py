idadetot = 0
hmv = ''
ihmv = 0
mav = 0

for pessoa in range(0, 4):
    print(f'----- {pessoa + 1}ª PESSOA -----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').upper().strip()

    idadetot += idade

    if sexo == 'M':
        if idade > ihmv:
            ihmv = idade
            hmv = nome
            
    elif sexo == 'F':
        if idade < 20:
            mav += 1

idademed = idadetot / 4 #média de idade do grupo

print(f'A média de idade do grupo, é de {idademed:.1f} anos.')

if ihmv > 1:
    print(f'O homem mais velho é o {hmv} que tem {ihmv}.')
else:
    print(f'O grupo não possui nenhum homem')

if mav > 1:
    print(f'Ao todo, são {mav} mulheres com menos de 20 anos.')
elif mav ==1:
    print(f'Ao todo, o grupo possui penas uma mulher com menos de 20 anos.')
elif mav == 0:
    print(f'O grupo não possui nenhuma mulher com menos de 20 anos.')
