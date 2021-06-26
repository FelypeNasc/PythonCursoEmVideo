print('=-=' *16)
print(' ' * 10, 'Analisador de triângulos')
print('=-=' *16)

s1 = float(input('Digite o valor do primeiro segmento: '))
s2 = float(input('Digite o valor do segundo segmento: '))
s3 = float(input('Digite o valor do terceiro segmento: '))

if s1 >= s2 + s3 or s2 >= s1 + s3 or s3 >= s1 + s2:
    print('Os valores acima NÃO formam um triângulo!')
elif s1 == s2 == s3:
    print('Os valores acima PODEM formar um triângulo EQUILÁTERO')
elif s1 != s2 != s3 != s1:
    print('Os valores acima PODEM formar um triângulo ESCALENO')
else:
    print('Os valores acima PODEM formar um triângulo ISÓSCELES')