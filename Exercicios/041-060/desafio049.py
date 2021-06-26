# crie um código que leia um número e faça a tabuada dele até 10
print('---------TABUADA---------')
print('')
num = int(input('Digite o número: '))
for n in range(1, 11):
    res = num * n
    print(f'{num}x{n}= {res}')