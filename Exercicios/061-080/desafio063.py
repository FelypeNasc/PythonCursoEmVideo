print('-=' * 15)
print(' ' * 3, 'SEQUÊNCIA DE FIBONACCI')
print('-=' * 15)

n = int(input('Quantos números deseja ver? '))
cont = 0

n1 = 1
n2 = 1
n3 = None
print(f'{n1} ➞ ', end='')
while n > cont +1:
    n3 = n1 +n2
    n1 = n2
    n2 = n3
    cont += 1
    print(f'{n1} ➞ ', end='')

print('FIM')