#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e converta para dólar (dólar = 5.36)
brl = float(input('Quanto dinheiro você tem na carteira? '))
usd = 5.36
brltousd = brl/usd

print('Você tem: R${} \n'
      'Conversão para dólar: U${:.2f} \n'
      .format(brl, brltousd)
      )