# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# E a quantidade de dias pelos quais ele foi alugado.
# R$60/dia e R$0,15/km rodado.

dias = int(input('Quantos dias ficou com o carro? '))
kms = int(input('Quantos kms foram rodados? '))

aluguel = dias*60+kms*0.15
print('O valor total a ser pago é: R${}' .format(aluguel))
