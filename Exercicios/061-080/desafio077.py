wordList = ('empatia', 'embuste', 'cônjuge', 'exceção', 'efêmero', 'prolixo', 'idílico', 'caráter', 'análogo')
vowels = ('aáãeéêiíîoóôõuúû')
print('Palavras e suas vogais')
for word in wordList:
    print(f'{word.capitalize()}:', end= ' ')
    for letter in word:
        if letter in vowels:
            print(f'{letter.capitalize()}', end=' ')
    print('')