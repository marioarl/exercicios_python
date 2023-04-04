'''
Credito : https://wiki.python.org.br/ExerciciosFuncoes ref: Ex funcoes 8

Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.    
'''
from os import system
from colorama import Fore, init
init(autoreset=True)
system('cls')

def qtdDigitos(num):
    return len(str(num))

def contarDigitos(n): #Funcao utilizando While e um contador
    contador = 1
    while n >=10:
        n = n // 10
        contador += 1
    return contador

n = int(input('Digite um numero inteiro: '))
print(f'O numero {n} contém {qtdDigitos(n)} digitos')
print(f'O numero {n} contém {contarDigitos(n)} digitos')
