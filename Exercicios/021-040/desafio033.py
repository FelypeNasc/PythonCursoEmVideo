# Crie um código que leia 3 número e mostre qual é o maior e qual é o menor
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 > n2:
    if n1 > n3:
        maiorNum = n1
    else:
        maiorNum = n2
else:
    maiorNum = n2

print(f'O maior número é {maiorNum}')

if n1 < n2:
    if n1 < n3:
        menorNum = n1
    else:
        menorNum = n2
else:
    menorNum = n2

print(f'O menor número é {menorNum}')





