lista = list()

for pos in range (0, 5):
    lista.append(int(input(f'Digite um número para a posição {pos}: ')))

print(f'O menor valor digitado foi {min(lista)} nas posições ', end='')

for pos, num in enumerate(lista):
    if num == min(lista):
        print(f'{pos}, ', end= '')

print(f'\nO maior valor digitado foi {max(lista)} nas posições ', end='')

for pos, num in enumerate(lista):
    if num == min(lista):
        print(f'{pos}, ', end= '')