'''
Credito : https://wiki.python.org.br/EstruturaSequencial ref: Ex listas 12

Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
'''
from os import system
from random import randrange, uniform
system('cls')


idade = []
altura = []
alunoM13 = []
media_13 = []

for i in range(30):
    idadeAleatorio = idade.append(randrange(1, 20))
    alturaAleatorio = altura.append(uniform(1, 2))

for i in range(30):
    if idade[i] > 13:
        alunoM13.append(altura[i])

media = sum(alunoM13) / len(alunoM13)

for i in range(len(alunoM13)):
    if alunoM13[i] < media:
        media_13.append(alunoM13[i])
print('='*60)
print('RESUMO'.center(60))
print('='*60)
print(f'Idade dos alunos............: {idade}')
print(f'Altura dos alunos (cm)......: {altura}')
print(f'Alunos acima de 13 anos.....: {len(alunoM13)} -> Alturas: {alunoM13}')
print(f'Media de altura.............: {media}')
print(f'Alunos acima de 13 anos abaixo da média de altura: {len(media_13)} -> {media_13}')
