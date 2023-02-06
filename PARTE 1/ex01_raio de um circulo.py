'''
Credito : https://wiki.python.org.br/EstruturaSequencial
Faça um programa que peça o raio de um circulo, calcule e mostre sua área
'''
from math import pi
r = float(input('Digite o raio do circulo: '))
area = pi * (r**2)
print(f'A area do circulo de raio {r} é igual {area:.2f}')