expre = list(input('Digite uma expressão matemática: '))
parent = 0

for n in expre:
    if n == '(':
        parent += 1
    elif n == ')':
        parent -= 1
    if parent < 0:
        break

if parent == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
# (1+2)+(2+1))