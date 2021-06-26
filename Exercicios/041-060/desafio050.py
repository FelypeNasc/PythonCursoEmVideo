# crie um código que leia 6 números e mostre as somas entre os números ímpares e a soma dos números pares
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 ==0:
        cont += num

print('A soma dos números pares entre os digitados foi de {}' .format(cont))
