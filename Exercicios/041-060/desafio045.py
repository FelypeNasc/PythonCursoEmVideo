#crie um código de jokenpô
# 1= pedra 2= papel 3= tesoura
from random import randint
from time import sleep
print('-=' * 10)
print(' '* 5, 'JOKENPÔ')
print('-=' * 10)
jogador = int(input('''
[ 1 ] Pedra 
[ 2 ] Papel 
[ 3 ] Tesoura 

Escolha: '''))
computador = randint(1,3)

sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!')

if jogador == 1:
    jogador = 'pedra'
elif jogador == 2:
    jogador = 'papel'
elif jogador == 3:
    jogador = 'tesoura'
else:
    print('ESCOLHA INVÁLIDA')

if computador == 1:
    computador = 'pedra'
elif computador == 2:
    computador = 'papel'
elif computador == 3:
    computador = 'tesoura'

print('-=' * 15)
print(f'Jogador jogou {jogador.capitalize()}')
print(f'Computador jogou {computador.capitalize()}')
print('-=' * 15)

if jogador == computador:
    print('EMPATE!')
elif jogador == 'tesoura' and computador == 'papel' or jogador == 'papel' and computador == 'pedra' or jogador == 'pedra' and computador == 'tesoura':
    print('JOGADOR VENCEU!')
elif computador == 'tesoura' and jogador == 'papel' or computador == 'papel' and jogador == 'pedra' or computador == 'pedra' and jogador == 'tesoura':
    print('COMPUTADOR VENCEU!')
