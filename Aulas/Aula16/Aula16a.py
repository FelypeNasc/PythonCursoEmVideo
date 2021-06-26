# TUPLAS = SÃO IMUTÁVEIS
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
print (lanche[1])
print (lanche[2:])

for comida in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[comida]}')

for comida in lanche:
    print (f'Eu vou comer {comida}')

for pos, comida in enumerate(lanche):
    print (f'Eu vou comer {comida} na posição {pos}')
