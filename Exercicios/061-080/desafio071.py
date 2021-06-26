sacar = int(input('Quanto deseja sacar? R$ '))

not50 = not20 = not10 = not1 = 0

while sacar >= 50:
    sacar -= 50
    not50 += 1

while sacar >= 20:
    sacar -= 20
    not20 += 1

while sacar >= 10:
    sacar -= 10
    not10 += 1

while sacar >= 1:
    sacar -= 1
    not1 +=1

print(f'Notas de R$50: {not50}')
print(f'Notas de R$20: {not20}')
print(f'Notas de R$10: {not10}')
print(f'Notas de R$1: {not1}')