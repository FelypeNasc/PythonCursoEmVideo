# crie um código que leia a altura e peso de uma pessoa e diga seu imc e sua categoria
print('-=-' * 10)
print(' ' * 5, 'Calculadora de IMC')
print('-=-' * 10)
print('')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso/(altura**2)

if imc < 18.5:
    print(f'Seu IMC é de {imc:.1f}. Classificação: Abaixo do peso')
elif imc < 25:
    print(f'Seu IMC é de {imc:.1f}. Classificação: Normal')
elif imc < 30:
    print(f'Seu IMC é de {imc:.1f}. Classificação: Sobrepeso')
elif imc < 35:
    print(f'Seu IMC é de {imc:.1f}. Classificação: Obesidade Grau I')
elif imc <40:
    print(f'Seu IMC é de {imc:.1f}. Classificação: Obesidade Grau II')
else:
    print(f'Seu IMC é de {imc:.1f}. Classificação: Obesidade Grau III ou Mórbida')
