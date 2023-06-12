'''
Credito : https://wiki.python.org.br/ExerciciosListas Ex6

Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
'''

from os import system
from colorama import Fore,init
init(autoreset=True)
system('cls')
medias = []
cont = 0
for a in range(1,11):
    media = somaNota = 0
    print(f'{Fore.YELLOW}Digite as 4 notas do aluno {a}')
    for n in range(1,5):
        nota = float(input(f'{Fore.GREEN} - Digite a {n}a. nota: '))
        somaNota += nota
    media = somaNota / 4
    medias.append(media)
    system('cls')
print(f'{"Aluno":<10}{"Média":>5}')
for i, m in enumerate(medias):
    print(f'{i+1:<10}{m:>5.2f}')
    if m >=7:
        cont += 1

print(f'Quantidade de alunos com média igual ou superior a 7 : {cont}')
