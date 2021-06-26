# crie um código de uma loja que receba o valor da compra e dê preços diferentes de acordo com o tipo de pagamento
# à vista/cheque 10% off / á vista no cartão 5% off /  até 2x no cartão 0% / 3x ou mais no cartão 20% de juros
print('============ Lojas do Caralho ============')
valor = float(input('Preço das compras: R$'))
print('')
formPag = int(input('''FORMAS DE PAGAMENTO
[ 1 ] Dinheiro 
[ 2 ] Cartão
Digite sua opção: '''))
print('')
if formPag == 1:
    aPagar = valor * 0.90
    print(f'TOTAL À PAGAR: R${aPagar:.2f}. (10% de desconto)')
elif formPag == 2:
    parcelOpt = int(input('''À VISTA OU PARCELAR?
[ 1 ] À vista
[ 2 ] Parcelar
Digite sua opção: '''))
    print('')
    if parcelOpt == 1:
        aPagar = valor * 0.95
        print(f'TOTAL À PAGAR: R${aPagar:.2f}. (5% de desconto)')
    elif parcelOpt == 2:
        parcelVezes = int(input('''EM QUANTAS VEZES? (até 10x)
Digite sua opção: '''))
        print('')
        if parcelVezes <= 2:
            aPagar = valor
            print(f'TOTAL À PAGAR: R${aPagar:.2f} em 1x.')
        elif 3 >= parcelVezes <= 10:
            aPagar = valor * 1.20
            parcelValor = valor / parcelVezes
            print(f'''TOTAL À PAGAR: R${aPagar:.2f} (20% de juros)
PARCELAMENTO: {parcelVezes} vezes de R${parcelValor:.2f}.''')
        else:
            print('ERRO: VALOR INVÁLIDO')
    else:
        print('ERRO: VALOR INVÁLIDO')
else:
    print('ERRO: VALOR INVÁLIDO')


