sexo = input('Sexo (M/F): ').strip().upper()[0]

if sexo != 'F' and sexo != 'M':
    while sexo not in 'MmFf':
        print('Opção inválida, digite novamente.')
        sexo = input('Sexo (M/F): ').strip().upper()

if sexo == 'M':
    print('Você é do sexo masculino.')
else:
    print('Você é do sexo feminino. ')