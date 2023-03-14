'''
Credito : https://wiki.python.org.br/EstruturaSequencial ref: Ex funcoes 9

Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.   
'''
from os import system
system('cls')

def inverso(num):
    x = str(num)
    rev = x[::-1]
    return rev

n = int(input('Digite um número inteiro: '))
print(f'O reverso do numero digitado {n} é {inverso(n)}')
