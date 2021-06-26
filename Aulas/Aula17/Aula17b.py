valores = list()

for n in range(0,5):
    valores.append(int(input('Digite um número: ')))

for pos, value in enumerate(valores):
    print(f'Na posição {pos} foi digitado o número {value}!')

a = [1, 3, 5, 6]
b = a[:]
b[2] = 67

print(f'Lista A: {a}')
print(f'Lista B: {b}')