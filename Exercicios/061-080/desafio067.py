print('-=' * 10)
print(' ' * 4, 'Tabuada')
print('-=' * 10)

num = 0

while True:
    print('-' * 40)
    num = int(input('Digite um número para saber sua tabuada: '))
    print('-' * 40)
    if num < 0:
        break

    for n in range(1, 11):
        print(f'{num} X {n} = {num * n} ')

print('FIM!')
