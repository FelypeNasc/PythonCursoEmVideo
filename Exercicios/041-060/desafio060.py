numinit = int(input('Digite um número para saber seu fatorial: '))
num = numinit
calc = 1
print(f'O fatorial de {numinit}: ')
while num > 0:
    print(f'{num}', end='')
    print(' x ' if num != 1 else ' = ', end='')
    calc = calc * num
    num -= 1

print(f'{calc}')