# Crie um código que leia uma frase, diga quantos "A"s tem nela, qual é a posição do primeiro A e do último A
frase = str(input('Digite uma frase: ')).lower().strip()
numA = frase.count('a')
posA = frase.find('a')+1
posUltA = frase.rfind('a')+1
print('Essa frase contém {} letras A. ' .format(numA))
print('A primeira letra A aparece na posição {} ' .format(posA))
print('A última letra A aparece na posição {}' .format(posUltA))

