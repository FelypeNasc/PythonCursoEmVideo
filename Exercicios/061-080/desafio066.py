num = soma = cont = 0
while True:
    num = int(input('Digite um número (-1 para parar): '))
    if num == -1:
        break
    cont += 1
    soma += num

if cont == 0:
    print(f'Não foi digitado nenhum valor.')
elif cont == 1:
    print(f'Foi digitado apenas o número {soma}.')
else:
    print(f'A soma dos {cont} números é {soma}.')
