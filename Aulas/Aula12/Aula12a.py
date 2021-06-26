# aula sobre condições aninhadas (compostas) aka if elif else

nome = str(input('Digite seu nome: '))
if nome == 'Felype':
    print('Que nome bonito!')
elif nome == 'Thayná' or nome == 'Thayna' or nome == 'Thayninha' or nome == 'Xulu':
    print('Uhm, então você é um pitelzinho. :B')
elif nome in 'Maria João Matheus':  # pode ser usado no lugar de or dentro da estrutura if
    print('Seu nome é bem normal no Brasil.')
else:
    print('Que nome normal que você tem')

print (f'Tenha um bom dia, {nome}!')

