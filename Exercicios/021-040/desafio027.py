# Crie um código que leia um nome completo, diga quantos nomes a pessoa tem, qual é o primeiro e último nome dela.
nome = str(input('Digite seu nome completo: ')).split()
primNome = nome[0].title()
ultNome = nome[-1].title()
qntNome = len(nome)
print('Você tem {} nomes' .format(qntNome))
print('Seu primeiro nome é: {}' .format(primNome))
print('Seu último nome é: {}' .format(ultNome))
