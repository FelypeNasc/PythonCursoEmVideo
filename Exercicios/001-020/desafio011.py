#Faça um programa que leia a largura e altura de uma parede
#Calcule sua área e calcule quantos litros de tinta serão necessários para pintá-la (cada litro=2m²)
print('Calculadora de tinta para parede')
wallH = float(input('Digite a altura da parede: '))
wallW = float(input('Digite a largura da parede: '))
area = wallH*wallW
tintLit = 2
tintQuant = area/tintLit
print('A área da parede é de {}m², será necessários {:.1f}l de tinta' .format(area, tintQuant))

