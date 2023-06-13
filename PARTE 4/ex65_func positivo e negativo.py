'''
Credito : https://wiki.python.org.br/ExerciciosFuncoes ref: Ex funcoes 4

Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere P se seu argumento for positivo, e N, se seu argumento for zero ou negativo.
'''

from os import system
system('cls')

def pos_neg(n):
    if n % 2 == 0:
        print('P')
    else:
        print('N')


pos_neg(8)
