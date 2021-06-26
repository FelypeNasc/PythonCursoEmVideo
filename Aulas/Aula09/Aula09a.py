# Análise com len(), count(), find(), transformações com replace(),
# upper(), lower(), capitalize(), title(), strip(), junção com join().
frase = """Curso em Video Python"""
frasecomespacos ='       dale dale   '

print(frasecomespacos)
print(frasecomespacos.strip())
print(frase[:13:2])
print(frase.count('o')) #conta quantos
print(frase)
print(len(frase))
print(frase.replace('Curso', 'Cursinho'))

# única forma de mudar uma str
frase = frase.replace('Python', 'Jogo do Bicho')
print(frase)

# Para fatiar uma frase e escolher uma letra se usa frase[3] por exemplo.
# Para mostrar a frase do início ao 3 caractere por exemplo, usa-se print(frase[:3]), lembrando que o primeiro caractere sempre é o 0
# Para mostrar do 3 caractere ao final usa-se print(frase[3:])
# O comando [::2] por exemplo, vai mostrar do início ao final pulando de 2 em 2
# O comando [3::2] por exemplo, serve para o python escrever do 3 ao final pulando de 2 em 2, mostrando o 2 (exemplo: ABCDEFGHI ficaria DFH)
# O comando len(frase) serve para indicar a quantidade de caracteres na frase já atribuida por um input, por exemplo
# O comando frase.count('o') por exemplo, serve para o python contar quantas vezez o ''o'' apareceu na frase
# No fatiamento o último valor sempre é ignorado pelo python.
# O comando frase.find('deo') serve para indicar onde começou o deo na frase ''curso em video'' por exemplo, sendo igual a 11
# Quando mandamos o python procurar algo que não existe na frase ele te da como resultado -1, indicando que aquilo não está na frase. Exemplo: print(frase.find('cagão') da frase cherapeido não existe, logo, ele vai ter como resultado -1
# O operador in serve para indicar se existe aquela parte já associada na frase também já associada. Ex: print(parte in frase)
# O comando frase.replace('python , 'android') por exemplo, serve para substituir o python da frase já associada por android. Ex: print(frase.replace('python, 'android') da frase já associada: curso em vídeo python
# O comando frase.upper() serve para deixar todas as letras da frase, já associada, mas, letras já em maiúsculas continuam em maiúsculas
# O comando frase.lower() deixa as letras maiúsculas em minúsculas, minúsculas permanecem em minúsculas
# A função frase.capitalize() serve para deixar todos os caracteres da frase já associada para minúsculo e deixar somente a primeira letra em maiúsculo
# O comando frase.title() serve para deixar as letras após espaços em maiúsculas
# A função frase.strip() remove todos os espaços inúteis, os entre palavras e letras continuam.
# A função frase.rstrip() retira os espaços da direta, final do texto
# A função frase.lstrip() retira os espaços da esquerda, início do texto
# A função frase.split() serve para separar as palavras em diferentes famílias de micro-memórias
# A função '-'.join(frase) por exemplo, serve para juntar famílias de micro-memórias com o que esta entre as aspas
# A função print com """ """serve para o python escrever do mesmo modo que foi escrito, com quebras de linhas, bom para textos grandes.
# Quando usamos o comando frase.split() associado a dividido por exemplo, em uma frase já associada, o comando print(dividido[0]) mostrará a primeira família de micro-memórias, 1 a segunda, 2 a terceira e assim em diante