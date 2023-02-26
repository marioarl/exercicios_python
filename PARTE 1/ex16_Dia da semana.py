'''
Credito : https://wiki.python.org.br/EstruturaSequencial
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
'''
from colorama import Fore, init
init(autoreset=True)
dias = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")

n = int(input('Digite um numero correspondente ao dia da semana: '))
if n >=0 and n <=7:
    print(f'O dia da semana digitado foi {Fore.GREEN}{dias[n-1]}')
else:
    print(Fore.RED + 'Valor inválido')