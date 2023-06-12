'''
Credito : https://wiki.python.org.br/ExerciciosListas ref: Ex listas 9

Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
'''

from os import system
system('cls')

a = []
somaQuadrado = 0

for n in range(1,11):
    numero = int(input(f'Digite o {n}o. número: '))
    a.append(numero)
    somaQuadrado += numero ** 2

print(f'Os numeros digitados foram: {a}')
print(f'A soma dos quadrados dos elementos do vetor é: {somaQuadrado}')

