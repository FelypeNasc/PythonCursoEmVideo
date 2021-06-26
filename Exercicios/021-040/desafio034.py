# Crie um programa que leia um salário e calcule o valor do seu aumento
# Para salários acima de 1250,00, o aumento é de 10%. Abaixo disso, é de 15%.
print('----------------Verificando seu aumento----------------')
salar = float(input('Digite o seu salário: '))
if salar > 1250:
    aumento = salar*0.10
else:
    aumento = salar*0.15

print('Você ganhou um aumento de R${:.2f}. Seu novo salário é de R${:.2f}' .format(aumento, salar+aumento))