print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

productList = ('Bolete', 2.50,
               'Lua Cheia', 4.50,
               'Pirulito', 3.25,
               'Bolix', 1.00,
               'Yogurte 100', 6.50,
               '7 Belo', 6.25,
               'Balinha do Coração', 5.40,
               'Brazilian Coffe', 4.50)
for pos in range (0, len(productList)):
    if pos % 2 == 0:
        print (f'{productList[pos]:.<32} R$', end=' ')
    else:
        print(f'{productList[pos]:2.2f}')
print('-' *40)

