print('---' * 9)
print(' ' * 3, 'LOJAS SUPER BARATO')
print('---' * 9)

totProduct = totBuy = plusThousand = cheapestName = cheapestPrice = 0

while True:
    productName = input('Nome do produto: ').strip()
    productPrice = float(input('Preço: R$ '))
    totProduct += 1
    totBuy += productPrice

    if productPrice > 1000:
        plusThousand += 1

    if productPrice < cheapestPrice or totProduct == 1:
        cheapestName = productName
        cheapestPrice = productPrice

    continuar = ' '

    while continuar not in 'SN':
        continuar = input('Cadastrar mais algum produto? (S/N) ').upper()

    if continuar == 'N':
        break

print('--' * 20)
print(f'O total da compra foi {totBuy} com {totProduct} itens.')
print(f'Temos {plusThousand} itens(s) acima de R$1000')
print(f'O produto mais barato foi {cheapestName} no preço de {cheapestPrice}')
