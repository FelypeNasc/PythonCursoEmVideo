# Crie um código que leia um número e diga sua unidade, dezena, centena e milhar.
num = int(input('Digite um número inteiro: '))
unid = num // 1 % 10
deze = num // 10 % 10
cent = num // 100 % 10
milh = num // 1000 % 10

print('O número digitado tem: ')
print('Unidade: {}'.format(unid))
print('Dezena: {}'.format(deze))
print('Centena: {}'.format(cent))
print('Milhar: {}'.format(milh))