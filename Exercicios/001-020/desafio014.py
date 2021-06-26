#crie um código que leia uma temperatura em ºC e transforme para ºF e ºK

celsius = float(input('Digite a temperatura em ºC: '))
fahren = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print('A temperatura digitada equivale a:')
print('{}ºC' .format(celsius))
print('{}ºF' .format(fahren))
print('{}ºK' .format(kelvin))