'''
Credito : https://wiki.python.org.br/EstruturaSequencial ref: Ex listas 13

Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 Janeiro, 
2 Fevereiro, . . . ).

'''
from os import system
from random import randrange
system('cls')
temps = [randrange(10,40) for x in range(12)]
mes = ['Janeiro', 'fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto',
        'Setembro', 'Outubro', 'Novembro', 'Dezembro']
media = sum(temps) / 12
print('='*53)
print('TEMPERATURAS MÉDIAS MENSAIS'.center(53))
print('='*53)
for i, t in enumerate(temps):
        print(f'{mes[i]:<10}{t:>5}')


print('==== TEMPERATURAS ACIMA DA MÉDIA ANUAL - POR MÊS ====')
print(f'Média anual: {media:.1f}')
print(f'\n{"Mes":<10}{"Temperatura":>10}')
print(f'{"===":<10}{"===========":>10}')
for i, t in enumerate(temps):
    if t > media:
        print(f'{mes[i]:<10}{t:>5}')