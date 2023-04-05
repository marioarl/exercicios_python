'''
Credito : https://wiki.python.org.br/ExerciciosComStrings ref: Ex Com Strings 5

Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F
'''
from os import system
from random import randint
from colorama import Fore, init
init(autoreset=True)
system('cls')
cores = [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.CYAN, Fore.YELLOW]
num = randint(0,4)
nome = str(input('Digite seu nome:'))

for i in range(len(nome)):
    print(cores[num] + nome[:len(nome)-i])

    


