#faça um código que leia um salário e mostre um aumento de 15% do mesmo
funcSal = float(input('Digite seu salário: R$'))
salAument = funcSal+(funcSal*0.15)

print('Seu salário passou de R${:.2f} para R${:.2f}. Um aumento de 15%' .format(funcSal, salAument))