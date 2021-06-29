lista = list()

while True:
    novoNum = int(input('Digite um número (0 para parar): '))
    if novoNum == 0:
        break
    if novoNum in lista:
        print('O número digitado já foi adicionado à lista, digite outro número. ')
    else:
        print('Valor adicionado à lista!')
        lista.append(novoNum)
print('•'*50)
print(f'Você digitou os números {sorted(lista)}')
