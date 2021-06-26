primeiro = int(input('Digite o primeiro termo: '))
r = int(input('Razão da PA: '))
calc = primeiro
term = 0

while term < 10:
    print(calc, '➞ ' if term < 9 else '➞ PAUSA', end='')
    term += 1
    calc += r

opt = None
qterm = term

while opt != 0:
    print('')
    opt = int(input('Quantos termos você quer mostrar a mais? '))
    qterm += opt
    while term < qterm:
        print(calc, '➞ ' if term < qterm-1 else '➞ PAUSA', end='')
        term += 1
        calc += r

print(f'Foram mostrados {qterm} termos.')