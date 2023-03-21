'''
Credito : https://wiki.python.org.br/EstruturaSequencial ref: Ex Com Strings 3

Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

F
U
L
A
N
O
'''
from os import system
system('cls')

nome = str(input('Digite seu nome:'))

for p in nome:
    print(p)


