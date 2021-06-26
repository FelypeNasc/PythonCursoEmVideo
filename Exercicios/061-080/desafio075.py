numTab = (int(input('1º número: ')),
          int(input('2º número: ')),
          int(input('3º número: ')),
          int(input('4º número: ')))

print (f'Os números digitados foram {numTab}')
nineCount = parCount = tresPos = 0

for n in numTab:
    if n == 9:
        nineCount += 1
    if 3 in numTab:
        tresFound = 1
        tresPos = numTab.index(3)+1
    if n % 2 == 0:
        parCount += 1
if nineCount == 0:

    print(f'O número 9 não foi digitado.')
else:
    print(f'O número 9 apareceu {nineCount} vezes.')

if tresFound == 0:
    print('O número 3 não foi digitado.')
else:
    print(f'O número 3 apareceu na {tresPos}º posição.')

if parCount == 0:
    print(f'Não foi digitado nenhum número par.')
else:
    print(f'Foram digitados {parCount} número(s) pares.')