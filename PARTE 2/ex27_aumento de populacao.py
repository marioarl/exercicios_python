'''
Credito : https://wiki.python.org.br/EstruturaSequencial
Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de crescimento de 3% 
e que a população de B seja 200.000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou 
iguale a população do país B, mantidas as taxas de crescimento.
'''
from colorama import Fore, init
init(autoreset=True)
a = 80000
b = 200000
anos = 0
while True:
    a += a * 3 / 100
    b += b * 1.5 / 100
    anos += 1
    if a >= b:
        break
print(f'O país A levará {Fore.CYAN}{anos} anos {Fore.RESET}para que se iguale ou supere a população do país B')