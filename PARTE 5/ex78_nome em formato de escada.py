'''
Credito : https://wiki.python.org.br/ExerciciosComStrings ref: Ex Com Strings 4

Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO
'''

from os import system
system('cls')

nome = str(input('Digite seu nome:'))
tamanho = len(nome)
for p in range(len(nome)):
    print(nome[0:p+1])


