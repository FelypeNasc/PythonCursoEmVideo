#faça um código que leia um preço e mostre-o com 5% de desconto

val = float(input('Digite o valor da mercadoria: R$'))
desconto = val-(val*0.05)

print('Com o desconto de 5%, o valor do produto passou de R${:.2f} para R${:.2f}.' .format(val, desconto))
