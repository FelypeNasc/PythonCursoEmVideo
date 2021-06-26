# crie um código que leia uma string e verifique se ela é um palíndromo

frase = input('Digite uma frase: ').strip().lower().replace(' ', '')
invertido = ''

for letra in range(len(frase)-1, -1, -1):
    invertido += frase[letra]

print(f'O inverso do "{frase}", é "{invertido}"')

if frase == invertido:
    print('Essa frase é um PALÍNDROMO. ')
else:
    print('Essa frase NÃO é um PALÍNDROMO.')
