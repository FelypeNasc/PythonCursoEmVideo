# Escreva um programa para aprovar um empréstimo para compra de uma casa.
# Leia o valor da casa, o salário do comprador e em quantos meses ele vai pagar.
# Calcule o valor da prestação, sabendo que ela não pode exceder 30% do salário ou será negado.
from time import sleep
print('=-=-='*10)
print(' ' *5, 'Simulador de financiamento residencial')
print('=-=-='*10)

cltName = str(input('Para prosseguir, digite seu nome: ')).strip().title()
valorCasa = float(input(f'Olá, {cltName}! Valor do imóvel: R$'))
cltSal = float(input('Digite qual é o seu salário : R$'))
emprTempo = int(input('Em quantos anos deseja pagar? '))
entrada = float(input('Digite o valor da entrada (Digite 0 caso não deseje):'))

minimo = cltSal*0.30
emprestValor = (valorCasa - entrada) * 1.10
parcelValor = emprestValor / (emprTempo * 12)

if parcelValor < minimo:
    print(f'Parabéns {cltName}, seu empréstimo foi APROVADO!')
    print(f"A casa, no valor de R${valorCasa} pode ser paga em:\n"
          f"    \n"
          f"Com parcelas de R${parcelValor:.2f} em {emprTempo * 12} meses, totalizando {emprestValor:.2f}\n")

else:
    print(f'Um imóvel de {valorCasa:.2f} pago em {emprTempo} daria uma parcela de {parcelValor:.2f}, sendo maior que '
          f'30% do seu salário! \n '
          f'Seu empréstimo foi NEGADO! :c ')

print('')
print('Até mais!')
