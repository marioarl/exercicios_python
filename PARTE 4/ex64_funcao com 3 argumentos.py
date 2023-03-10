'''
Credito : https://wiki.python.org.br/EstruturaSequencial ref: Ex funcoes 3

Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
'''
from os import system
system('cls')

def soma(a=1,b=1,c=1):
    r = a + b + c
    return r


print(soma(5))
