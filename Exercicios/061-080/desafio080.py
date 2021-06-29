lista = list()

for pos in range(5):
    num = int(input('Digite um valor: '))
    if pos == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista.')
    else:
        index = 0
        while index < len(lista):
            if num <= lista[index]:
                lista.insert(index, num)
                print(f'Valor adicionado na posição {index}.')
                break
            index += 1

print('•' * 50)
print(f'Valores em ordem: {lista}')
