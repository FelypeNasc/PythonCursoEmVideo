lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um número: ')))
    resp = input('Deseja continuar? [S/N] ')
    while resp not in 'SsNn':
        resp = input('Resposta inválida! \nDeseja continuar? [S/N] ')
    if resp in 'Nn':
        break

for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'Os valores digitados foram: {lista}')
print(f'Os valores pares digitados foram: {sorted(pares)}')
print(f'Os valores impares digitados foram: {sorted(impares)}')
