import random
from time import sleep
print('-------- ADIVINHE O NÚMERO --------')
input('')
print('Pensei em um número de 1 a 5, tente adivinhar!')
sleep(1)

computador = random.randint(1, 5)
jogador = int(input('Digite um número: '))
tentativa = 0

if jogador > 0 or jogador < 6:
    while jogador != computador:
        jogador = int(input('Você errou! Tente de novo: '))
        tentativa += 1
else:
    print('ERRO, TENTE NOVAMENTE!')

if tentativa == 0:
    print('Você acertou de primeira! BOA!')
else:
    print(f'Você acertou na sua {tentativa+1}º tentativa!')
