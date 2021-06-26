primeiro = int(input('Digite o primeiro termo: '))
r = int(input('Razão da PA: '))
calc = primeiro
term = 0

while term < 10:
    print(calc, '➞ ' if term < 9 else '', end='')
    calc += r
    term += 1
