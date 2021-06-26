# Crie um código que leia 2 número, diga qual deles é maior ou se são iguais

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('O PRIMEIRO número é o maior.')
elif num2 > num1:
    print('O SEGUNDO número é o maior.')
else:
    print('Os dois número são iguais!')