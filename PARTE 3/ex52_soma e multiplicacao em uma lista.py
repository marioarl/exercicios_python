'''
Credito : https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
'''
from colorama import Fore, init
init(autoreset=True)
from os import system
system('cls')
soma = 0
mult = 1

numeros = []
for n in range(1,6):
    num = int(input(f'{n}o. numero: '))
    soma += num
    mult *= num
    numeros.append(num)
print(f'Os numeros digitados foram: {Fore.RED}{numeros}')
print(f'Soma dos numeros...........: {Fore.GREEN}{soma}')
print(f'Multiplicação dos numeros..: {Fore.CYAN}{mult}')
