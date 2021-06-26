# Crie um código que leia o nome de uma cidade e veja se ela começou com a palavra "Santo"
cid = input('Em qual cidade você nasceu?').strip()
verif = cid[:5].lower() == 'santo'
print('Sua cidade começa com o nome "Santo"? {}'.format(verif))
