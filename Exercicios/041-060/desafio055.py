menor = 0
maior = 0

for pessoa in range(0, 5):
    peso = float(input(f'Peso da {pessoa+1}º pessoa: '))
    if pessoa == 0:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O menor peso registrado é de {menor}')
print(f'O maior peso registrado é de {maior}')
