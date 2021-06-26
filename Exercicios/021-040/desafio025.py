# Crie um código que leia um nome e veja de tem "Silva" nele.
nome = str(input('Qual é o seu nome?')).strip().upper().split()
print('Seu nome tem Silva? {}' .format('SILVA' in nome))
