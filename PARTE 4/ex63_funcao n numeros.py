'''
Credito : https://wiki.python.org.br/EstruturaSequencial ref: Ex funcoes 1

Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
'''
from os import system
system('cls')

def numeros(n):
    for i in range(1, n+1):
        print((str(i) + " ")*i)



n = int(input('Digite um numero: '))
numeros(n)

