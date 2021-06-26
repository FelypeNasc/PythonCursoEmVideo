#Faça um progrmaa que leia um número inteiro e mostre na tela o seu anterior e o próximo
num = int(input('Insira um número: '))
ant = num-1
sus = num+1
print ('O anterior ao número {} é o {}, e o próximo é {}.' .format(num, ant, sus))