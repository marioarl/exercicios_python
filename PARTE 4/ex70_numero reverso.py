'''
Credito : https://wiki.python.org.br/ExerciciosFuncoes ref: Ex funcoes 9

Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.   
'''
from os import system
from colorama import Fore, init
init(autoreset=True)
system('cls')

def inverso(num):
    x = str(num)
    rev = x[::-1]
    return rev

n = int(input('Digite um número inteiro: '))
print(f'O reverso do numero digitado {n} é {Fore.YELLOW}{inverso(n)}')
