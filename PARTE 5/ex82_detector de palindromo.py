'''
Credito : https://wiki.python.org.br/ExerciciosComStrings ref: Ex Com Strings 8

Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. 
A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre e diga se é um palíndromo ou não.
'''

from os import system
from colorama import Fore, init
init(autoreset=True)
system('cls')

frase = str(input('Digite uma frase: ')).strip().upper()
div = frase.split()
all = ''.join(div)
inverso = all[::-1]
print(f'O inverso de {frase} é {inverso}')

if inverso == all:
    print(Fore.GREEN + 'A frase é um PALINDROMO!')
else:
    print(Fore.RED + 'A frase NÃO É UM PALINDROMO!')
    


