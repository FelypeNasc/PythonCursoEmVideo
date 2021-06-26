# Crie um código que leia um número inteiro e converta ele para Binário, Octal e Hexadecimal

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para a conversão: 
Digite 1 para BINÁRIO
Digite 2 para OCTAL
Digite 3 para HEXADECIMAL''')
opt = int(input('Sua opção: '))

if opt == 1:
    print(f'O valor {num} convertido para binário é: {bin(num)[2:]}')
elif opt == 2:
    print(f'O valor {num} convertido para octal é: {oct(num)[2:]}')
elif opt == 3:
    print(f'O valor {num} convertido para hexadecimal é: {hex(num)[2:]}')
else:
    print('Opção inválida!')