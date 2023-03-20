'''
Credito : https://wiki.python.org.br/EstruturaSequencial ref: Ex Com Strings 2

Nome ao contrário em maiúsculas. 
Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas.
Dica: lembre que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.
'''
from os import system
system('cls')

nome = str(input('Digite seu nome: ')).strip()
print(nome.upper()[::-1])

