'''
Credito : https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
'''
from os import system
system('cls')
medias = []
cont = 0
for a in range(1,11):
    media = somaNota = 0
    print(f'Digite as 4 notas do aluno {a}')
    for n in range(1,5):
        nota = float(input(f' - Digite a {n}a. nota: '))
        somaNota += nota
    media = somaNota / 4
    medias.append(media)
    system('cls')
for m in medias:
    if m >=7:
        cont += 1

print(f'Quantidade de alunos com média igual ou superior a 7 : {cont}')