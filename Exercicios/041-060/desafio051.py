# crie um número que leia o primeiro termo e a razão de uma pa e mostre os 10 primeiros termos.

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
termoVal = a1
for termo in range(0, 11):
    print(termoVal, '➞ ', end=" ")
    termoVal = termoVal + r
print('FIM')


a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
decimo = a1 + (10 - 1) * r

for termo in range(a1, decimo + r, r):
    print(termo, '➞ ', end=" ")
print('FIM')

