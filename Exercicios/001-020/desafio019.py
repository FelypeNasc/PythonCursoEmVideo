# crie um código que leia 4 nomes e sorteie um deles
from random import choice
nom1 = str(input('Digite o primeiro nome: '))
nom2 = str(input('Digite o segundo nome: '))
nom3 = str(input('Digite o terceiro nome: '))
nom4 = str(input('Digite o quarto nome: '))
lista = [nom1, nom2, nom3, nom4]
nomEscolhido= choice(lista)

print('O nome sorteado foi {}' .format(nomEscolhido))