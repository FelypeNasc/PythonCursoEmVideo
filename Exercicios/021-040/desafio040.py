# Crie um programa que leia 2 notas de um aluno, faça uma média das notas
# E diga se ele está aprovado (se abaixo de 5), de recuperação (se entre 5 e 6.9) e aprovado (se 7 ou mais)

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print('Você está REPROVADO!')
elif 5 < media < 7:
    print('Você está de RECUPERAÇÃO!')
elif media > 6.9:
    print('Você está APROVADO!')
