# Crie um código que crie um número aleatório e faça com que uma pessoa tente acertar o número gerado.
import random
import time

num = int(random.randint(1, 5))
print('\033[0;31m-=-\033[m' * 20)
print('\033[1;36m          Uhmm... Pensei num número entre 1 e 5.\033[m')
print('\033[31m-=-\033[m' * 20)
guess = int(input('Tente adivinhar: '))
print('\033[33mProcessando...\033[m')
time.sleep(1)
if guess == num:
    print('\033[1;32mParabéns, você acertou!\033[m')
else:
    guess2 = int(input('\033[31mVocê errou!\033[m Tente mais uma vez: '))
    print('\033[33mProcessando...\033[m')
    time.sleep(1)
    if guess2 == num:
        print('\033[1;32mParabéns, você acertou!\033[m')
    else:
        guess3 = int(input('\033[31mVocê errou!\033[m Última chance: '))
        print('\033[33mProcessando...\033[m')
        time.sleep(1)
        if guess3 == num:
            print('\033[1;32mParabéns, você acertou!\033[m')
        else:
            print('\033[1;31mCarai, cê não acerta mesmo.\033[m')
print('Fim!')
time.sleep(3)
