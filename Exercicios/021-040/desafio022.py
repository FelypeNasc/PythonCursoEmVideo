# Crie um código que leia um nome, mostre esse nome com todas letras minúsculas, todas as letras maiúsculas,
# mostre quantas letras tem e diga qual é o primeiro nome da pessoa e conte quantas letras ele tem.
name = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')
print('Seu nome em maiúsculas é : {}' .format(name.upper()))
print('Seu nome em minúsculas é : {}' .format(name.lower()))
print('Seu nome tem ao todo {} letras.' .format(len(name) - name.count(' ')))
nameSplit = name.split()
print('Seu primeiro nome é {} e ele tem {} letras.' .format(nameSplit[0], len(nameSplit[0])))
