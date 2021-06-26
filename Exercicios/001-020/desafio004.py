# um script que diga várias informações do que foi digitado

val = input('Digite algo: ')

print('O que foi digitado é do tipo', type(val))
print('É um número?', val.isnumeric())
print('Tem letras?', val.isalpha())
print('É alfanumérico?', val.isalnum())
print('Está em letras maíusculas?', val.isupper())
print('Está em letras minúsculas?', val.islower())
print('Tem a primeira letra maiúscula?', val.istitle())