'''
Credito : https://wiki.python.org.br/EstruturaSequencial ref: Ex funcoes 12

Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres + , - e | . Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.
'''
from os import system
from time import sleep
from colorama import Fore, init
init(autoreset=True)
system('cls')


def desenha_retangulo(linhas=1, colunas=1):
    if linhas < 1:
        linhas = 1
    elif linhas > 20:
        linhas = 20
        print(Fore.RED + 'Desculpe, infelizmente só posso desenhar no máximo 20 linhas')
        sleep(2)
    if colunas < 1:
        colunas = 1
    elif colunas > 20:
        colunas = 20
        print(Fore.RED + 'Desculpe, infelizmente só posso desenhar no máximo 20 colunas')
        sleep(2)
    print('+' + '-'*(colunas-2) + '+')
    for i in range(linhas-2):
        print('|' + ' '*(colunas-2) + '|')
    print('+' + '-'*(colunas-2) + '+')

print('===== DESENHAR UM RETANGULO =====')
l = int(input('Digite o numero de linhas: '))
c = int(input('Digite o numero de colunas:'))
desenha_retangulo(l,c)