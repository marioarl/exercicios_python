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
from colorama import Fore, init
init(autoreset=True)
from random import randint
system('cls')

num = randint(0,4)
nome = str(input('Digite seu nome:'))

for p in nome:
    print(p)


