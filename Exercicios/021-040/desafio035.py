print('=-=' *20)
print('Analisador de triângulos')
print('=-=' *20)
s1 = float(input('Digite o valor do primeiro segmento: '))
s2 = float(input('Digite o valor do segundo segmento: '))
s3 = float(input('Digite o valor do terceiro segmento: '))

if s1 >= s2 + s3 or s2 >= s1 + s3 or s3 >= s1 + s2:
    print('Os valores acima NÃO formam um triângulo!')
else:
    print('Os valores acima podem formar um triângulo!')