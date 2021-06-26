from datetime import date
menor = 0
maior = 0

for pessoa in range(1, 8):
    nasc = int(input(f'Em que ano a {pessoa}º pessoa nasceu? '))
    idade = date.today().year - nasc
    if idade >= 21:
        maior += 1
    elif idade < 21:
        menor += 1

print(f'Dentre essas pessoas, {menor} são menores de idade e {maior} maiores de idade.')