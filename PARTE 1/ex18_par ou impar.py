'''
Credito : https://wiki.python.org.br/EstruturaDeDecisao Ex22
Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
'''
from colorama import  Fore, init
init(autoreset=True)
num = int(input('Digite um numero: '))
print(f'O numero {num} digitado é ', end="")
if num % 2 == 0:
    print(Fore.BLUE + "PAR")
else:
    print(Fore.RED + "IMPAR")