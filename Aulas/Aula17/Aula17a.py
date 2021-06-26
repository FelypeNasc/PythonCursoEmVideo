# Listas Tuplas () Listas []

lista = ['cookie', 'pizza', 'suco', 'hamburguer']
lista.append('refri')
# Adiciona no final da lista o valor referido

lista[1] = 'pizza de queijo'

lista.insert(3, 'iced tea')
# Adiciona na posição referida o valor referido e o restante é colocado pra frente

del lista[0]
# Comando para deletar uma posição da lista

lista.pop()
# Deleta a última posição da lista ou a posição referida
if 'suco' in lista:
    lista.remove('suco')
# Deleta o valor referido independemente da posição

print(lista)

valores = list(range(0, 11))
valores.sort(reverse=True)
# Ordena do maior pro menor
print(valores)

valoresB = [2, 4, 6, 9, 0, 2]
valoresB.sort()
print(valoresB)
