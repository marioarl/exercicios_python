'''
Credito : https://wiki.python.org.br/EstruturaSequencial ref: Ex listas 12

Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
'''
from os import system
from colorama import Fore, init
init(autoreset=True)
from random import randrange, uniform
system('cls')


idade = [randrange(1,20) for i in range(30)]
altura = [format(uniform(1,2), '.2f') for a in range(30)]
altura_float = [float(x) for x in altura] # fazendo um cast de str para float
maior13 = []
media13 = []

for x in range(30):
    if idade[x] > 13:
        maior13.append(altura_float[x])

media = sum(maior13)/len(maior13)

for i in range(len(maior13)):
    if maior13[i] < media:
        media13.append(maior13[i])

print('='*60)
print('RESUMO'.center(60))
print('='*60)
print(f'Idade dos alunos..........: {Fore.YELLOW}{idade}')
print(f'Altura dos alunos (m).....: {Fore.BLUE}{altura_float}')
print(f'Alunos acima de 13 anos...: {Fore.GREEN}{len(maior13)}\033[m --> Alturas: {Fore.GREEN}{maior13}')
print(f'Média de altura...........: {Fore.RED}{media:.2f}')
print(f'Alunos acima de 13 anos abaixo da média de altura: {Fore.MAGENTA}{len(media13)} -> {media13}')
print()

