'''
Credito : https://wiki.python.org.br/EstruturaSequencial ref: Ex funcoes 8

Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.    
'''
from os import system
from colorama import Fore, init
init(autoreset=True)
system('cls')

def qtdDigitos(num):
    return len(str(num))

n = int(input('Digite um numero inteiro: '))
print(f'O numero {n} contém {qtdDigitos(n)} digitos')
