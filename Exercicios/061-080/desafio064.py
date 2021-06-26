cont = opt = soma = None
opt = int(input('Digite um número (0 para parar): '))
while opt != 0:
    soma += opt
    cont += 1
    opt = int(input('Digite um número (0 para parar): '))

print(f'Você digitou {cont} números e a soma entre eles, foi de {soma}')