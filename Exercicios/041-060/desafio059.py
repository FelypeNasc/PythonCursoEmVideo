from time import sleep
escolha = None
# quantNum = int(input('Digite quantos números deseja inserir: '))
print('--------VERIFICADOR DE NÚMEROS--------')
print('')

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

while escolha != 5:
    print('   ------ OPÇÕES ------')
    print(f'''    N1= {n1} N2= {n2}
    
 [1] Somar
 [2] Multiplicar
 [3] Verificar o maior
 [4] Mudar números
 [5] Sair do programa''')
    print('')
    escolha = int(input('Digite sua escolha: '))
    print('')

    if escolha == 1:
        soma = n1 + n2
        print(f'O resultado da soma é: {soma}')
        sleep(1)
        print('')

    elif escolha == 2:
        mult = n1 * n2
        print(f'O resultado da multplicação é {mult}')
        sleep(1)
        print('')
    elif escolha == 3:
        if n1 > n2:
            print(f'{n1} é o maior')
        elif n2 > n1:
            print(f'{n2} é o maior')
        else:
            print(f'{n1} e {n2} são iguais.')
        sleep(1)
        print('')

    elif escolha == 4:
        n1 = float(input(f'Digite o primeiro número: '))
        n2 = float(input(f'Digite o segundo número: '))
        sleep(1)
        print('')

print('-------- Programa finalizado --------')


