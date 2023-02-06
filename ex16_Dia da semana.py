'''
Credito : https://wiki.python.org.br/EstruturaSequencial
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
'''
dias = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")

n = int(input('Digite um numero correspondente ao dias da semana: '))
if n >=0 or n <=7:
    print(f'O dia da semana digitado foi {dias[n-1]}')