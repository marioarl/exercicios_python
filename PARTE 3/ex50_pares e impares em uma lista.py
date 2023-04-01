'''
Credito : https://wiki.python.org.br/ExerciciosListas Ex5

Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
'''
from colorama import Fore, init
init(autoreset=True)
numeros = []
impar = []
par = []

for n in range(1,21):
    num = int(input(f'{n}o. numero: '))
    numeros.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f'Os numeros digitados foram: {Fore.RED}{numeros}')
print(f'Numeros PARES...: {Fore.GREEN}{par}')
print(f'Numeros IMPARES.: {Fore.MAGENTA}{impar}')
    

