# crie um código que leia o valor de um ângulo e calcule o seno, cosseno e tangente
import math
ang = float(input('Digite o ângulo: '))
angC = math.radians(ang)
sen = math.sin(angC)
cos = math.cos(angC)
tan = math.tan(angC)

print('O ângulo de {}º tem as seguintes características:' .format(ang))
print('Seno: {:.2f}' .format(sen))
print('Cosseno: {:.2f}' .format(cos))
print('Tangente: {:.2f}' .format(tan))
