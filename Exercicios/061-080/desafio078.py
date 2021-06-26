lista = list ()

for n in range(0, 5):
    lista.append(int(input('Digite um número: ')))

print(f'Os números digitados foram: {lista}')
print(f'O maior número foi o{max(lista)}, digitado na {lista.index(max(lista))+1}º posição.')
print(f'O menor número foi o{min(lista)}, digitado na {lista.index(min(lista))+1}º posição.')