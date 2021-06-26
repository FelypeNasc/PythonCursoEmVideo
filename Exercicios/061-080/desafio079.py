lista = list()

while True:
    newNum = int(input('Digite um número (0 para parar): '))
    if newNum == 0:
        break
    if newNum in lista:
        print('O número digitado já foi adicionado.')
    else:
        lista.append(newNum)
