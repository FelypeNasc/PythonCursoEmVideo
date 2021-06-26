# Crie um código que leia uma distância de uma viagem em Km e calcule o preço da passagem.
# R$0,50 por Km até 200km, R$0,45 para viagens mais longas.
viagem = float(input('Qual é a distância da viagem em quilômetros? '))
if viagem <=200:
    valor = viagem*0.50
else:
    valor = viagem*0.45

print('Sua viagem de {}Kms, deu um valor de R${}.' .format(viagem, valor))
