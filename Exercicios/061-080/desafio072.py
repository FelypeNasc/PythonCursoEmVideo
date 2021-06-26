num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 
'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    usNum = int(input('Digite um número entre 0 e 20: '))
    if 0 <= usNum <= 20:
        break
    print('Valor inválido. ', end='')

print (f'Você digitou o número {num[usNum]}!')
