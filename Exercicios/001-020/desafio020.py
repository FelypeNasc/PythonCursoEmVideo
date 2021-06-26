# crie um código que leia 4 nomes e sorteie uma ordem com esses nomes
from random import shuffle
nom1 = str(input('Digite o primeiro nome: '))
nom2 = str(input('Digite o segundo nome: '))
nom3 = str(input('Digite o terceiro nome: '))
nom4 = str(input('Digite o quarto nome: '))
lista = [nom1, nom2, nom3, nom4]
shuffle(lista)
print('A ordem sorteada foi: {}' .format(lista))
