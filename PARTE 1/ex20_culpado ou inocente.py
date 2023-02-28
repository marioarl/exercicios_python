'''
Credito : https://wiki.python.org.br/EstruturaSequencial
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''
from os import system
cont = 0
p1 = str(input('1) Telefonou para a vitima?   [S/N]: ')).strip().upper()[0]
if p1 in "S":
    cont += 1
p2 = str(input('2) Esteve no local do crime?  [S/N]: ')).strip().upper()[0]
if p2 in "S":
    cont += 1
p3 = str(input('3) Mora perto da vitima?      [S/N]: ')).strip().upper()[0]
if p3 in "S":
    cont += 1
p4 = str(input('4) Devia para a vitima?       [S/N]: ')).strip().upper()[0]
if p4 in "S":
    cont += 1
p5 = str(input('5) Já trabalhou com a vitima? [S/N]: ')).strip().upper()[0]
if p5 in "S":
    cont += 1
print('A pessoa é ', end="")
if cont == 2:
    print('SUSPEITA')
elif cont == 3 or cont == 4:
    print('CUMPLICE')
elif cont == 5:
    print('ASSASINO')
else:
    print('INOCENTE')