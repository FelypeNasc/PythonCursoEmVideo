# crie um código que some os números ímpares múltiplos de 3 entre 1 e 500
soma = 0
quant = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        soma += num
        quant += 1

print(soma)
print(quant)