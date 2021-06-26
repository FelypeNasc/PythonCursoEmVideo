print('=' * 29)
fCount = maiorCont = mCont = 0
while True:
    print(' ' * 3, 'CADASTRO DE PESSOAS')
    print('=' * 29)

    idade = int(input('Idade: '))
    sexo = continuar = ' '

    while sexo not in 'FM':
        sexo = input('Sexo (F/M): ').upper()

    if sexo == 'F' and idade < 20:
        fCount += 1
    if idade > 18:
        maiorCont += 1
    if sexo == 'M':
        mCont += 1

    print('=' * 29)
    while continuar not in 'SN':
        continuar = input('Deseja cadastrar mais alguém? ').upper()
    print('=' * 29)

    if continuar == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {maiorCont}')
print(f'Total de mulheres com menos de 20 anos: {fCount}')
print(f'Total de homens cadastrados: {mCont}')