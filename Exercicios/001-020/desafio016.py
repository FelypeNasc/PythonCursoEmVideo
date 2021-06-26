# Crie um código que leia um número real e mostre na tela a sua porção inteira.
import math
num = float(input('Digite um número real (com vírgula): '))
nNum = math.trunc(num)
print('O número real {}, quando convertido para inteiro, é {}' .format(num, nNum))
