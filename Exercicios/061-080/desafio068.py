from random import randint

print("-=-" * 8)
print('  JOGO DE ÍMPAR OU PAR')
print("-=-" * 8)
print('')

winCont = 0

while True:
    computador = randint(1, 10)
    print('---' * 10)
    jogOpcao = ' '
    while jogOpcao not in 'IP':
        jogOpcao = str(input('Ímpar ou par? (I/P) ')).strip().upper()[0]

    jogador = int(input('Diga seu número: '))

    print('---' * 10)

    result = (jogador + computador) % 2
    print(f'Você jogou {jogador} e o computador jogou {computador}. A soma é {jogador+computador}, deu',
    'PAR! ' if result == 0 else 'ÍMPAR!')

    if result == 0:
        if jogOpcao in 'P':
            print('VOCÊ GANHOU!')
            winCont += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif result == 1:
        if jogOpcao in 'I':
            print('VOCÊ GANHOU!')
            winCont += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogador de novo...')

if winCont == None:
    print('GAME OVER! Você perdeu logo na primeira! PUTZ')
elif winCont == 1:
    print('GAME OVER! Você ganhou 1 vez!')
else:
    print(f'GAME OVER! Você ganhou {winCont} vezes!')
