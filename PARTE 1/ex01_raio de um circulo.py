'''
Credito : https://wiki.python.org.br/EstruturaSequencial Ex6
Faça um programa que peça o raio de um circulo, calcule e mostre sua área
'''

from colorama import Fore, init
init(autoreset=True)
from math import pi
r = float(input('Digite o raio do circulo: '))
area = pi * (r**2)
print(f'A área do circulo de raio {r} é igual {Fore.RED}{area:.2f}')