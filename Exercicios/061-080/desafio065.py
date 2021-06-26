opt = cont = tot = maior = menor = num = 0

while opt != 'N':
    num = int(input('Digite um número: '))
    tot += num
    cont += 1
    if cont == 1:
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    opt = str(input('Deseja continuar? (S/N) ')).upper().strip()

media = tot/cont

print(f'Você digite {cont} números e a média foi de {media}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')