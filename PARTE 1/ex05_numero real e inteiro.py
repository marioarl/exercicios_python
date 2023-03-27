'''
Credito : https://wiki.python.org.br/EstruturaSequencial
Faça um programa que peça 2 numeros inteiros e um numero real e inserir no input destes numeros o tratamento de erro. 
Calcule e mostre:
a) o produto do dobro do primeiro com a metade do segundo
b) a soma do triplo do primeiro com o terceiro
c) o terceiro elevado ao cubo
'''
from colorama import Fore, init
init(autoreset=True)
while True:
    try:
        numInteiro1= int(input('Digite o 1o. numero inteiro:'))
        break
    except ValueError:
        print(Fore.RED + 'ERRO!Digite um numero inteiro')

while True:
    try:
        numInteiro2= int(input('Digite o 2o. numero inteiro:'))
        break
    except ValueError:
        print(Fore.RED + 'ERRO!Digite um numero inteiro')

while True:
    try:
        numReal= float(input('Digite um numero Real:'))
        break
    except ValueError:
        print(Fore.RED + 'ERRO!Digite um numero inteiro')

print(f'A) O produto do dobro do primeiro com a metade do segundo: {(numInteiro1*2) * numInteiro2 / 2}')
print(f'B) A soma do triplo do primeiro com o terceiro: {(numInteiro1*3) + numReal}')
print(f'C) O terceiro elevado ao cubo: {numReal**2}')
