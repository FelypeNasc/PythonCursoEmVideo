# faça um código que leia os catetos de um triângulo retângulo e calcule a hipotenusa.
# catO = float(input('Digite o comprimento do cateto oposto: '))
# catA = float(input('Digite o comprimento do cateto adjacente: '))
# hipo = (catO ** 2 + catA ** 2) ** (1/2)
# print('A hipotenusa mede {}' .format(hipo))

from math import hypot
catO = float(input('Digite o comprimento do cateto oposto: '))
catA = float(input('Digite o comprimento do cateto adjacente: '))
hipo = hypot(catO, catA)
print('A hipotenusa mede {:.2f}' .format(hipo))