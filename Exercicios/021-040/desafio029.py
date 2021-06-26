# Crie um programa que leia uma velocidade e
print('Verificador de velocidade')
vel = float(input('Qual foi a velocidade em KM/H: '))
if vel > 80:
    multa = (vel-80)*7.00
    print('A velocidade está ACIMA do permitido. Você foi MULTADO em R${:.2f}.' .format(multa))
else:
    print('A velocidade está dentro do permitido!')