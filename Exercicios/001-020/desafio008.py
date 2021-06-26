#Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros

num = float(input('Digite o número de metros a ser convertirdo: '))
cent = num * 100
mili = num * 1000
print('{} metros equivalem em {:.0f}cm e {:.0f}mm' .format(num, cent, mili))
