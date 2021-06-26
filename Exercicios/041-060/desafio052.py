# crie um código que leia um número e diga se ele é um número primo

num = int(input('Digite um número: '))
cont = 0

for n in range(1, num+1):
    if num % n == 0:
        cont += 1
        print(f'\033[1;32m{n}\033[m ', end="")
    else:
        print(f'\033[1;31m{n}\033[m ', end="")
print('')

if cont == 2:
    print(f'O número {num} só é divisível por 1 e por ele mesmo.')
    print(f'Por isso, {num} o \033[1;32mé um número primo\033[m.')
else:
    print(f'O número {num} é divisível {cont} vezes.')
    print(f'Por isso, o {num} \033[1;31mNÃO\033[m é um número primo.')
