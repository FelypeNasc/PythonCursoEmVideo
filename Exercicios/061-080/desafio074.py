import random

numTab = (random.randint(0,100),
          random.randint(0,100),
          random.randint(0,100),
          random.randint(0,100),
          random.randint(0,100))

print(f'Os números sorteados foram: ', end='')
for n in numTab:
    print(n, end='')

sNumTab = sorted(numTab)
print (f'\nO menor número é: {sNumTab[0]}')
print (f'O menor número é: {sNumTab[-1]}')

