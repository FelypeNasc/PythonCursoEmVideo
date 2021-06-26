#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
num = int(input('Digite um número: '))
dob = num*2
tri = num*3
rai = int(num**0.5)
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {}.' .format(num, dob, tri, rai))
