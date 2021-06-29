lista = list()

while True:
    novoNum = int(input('Digite um número: '))
    lista.append(novoNum)
    resp = input('Deseja continuar? [S/N] ')
    while resp not in 'SsNn':
        resp = input('Resposta inválida! \nDeseja continuar? [S/N]')
    if resp in 'Nn':
        break

print('-=-' * 20)
print(f'Foram inseridos {len(lista)} números na lista.')
print('-' * 40)
print(f'Lista em ordem decrescente: {sorted(lista, reverse=True)}')
print('-' * 40)
print(f'O número 5 foi digitado na posição {lista.index(5)}' if 5 in lista else 'O número 5 não foi digitado')
