'''
Credito : https://wiki.python.org.br/EstruturaSequencial Ex14
Joao Papo-de -Pescador, homem de bem, comprou um computador para controlar o rendimento diário
de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento
de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$4,00 por quilo excedente.
Joao precisa que voce faça um programa que leia a variavel peso(peso dos peixes) e calcule o excesso.
Gravar na variavel excesso a quantidade de quilos alem do limite e na variavel multa o valor da multa 
que o Joao devera pagar. Imprima os dados do programa com as mensagens adequadas.
'''

from os import system
from colorama import Fore, Style, init
init(autoreset=True)
system('cls')
print(Fore.YELLOW + '*'*30)
print(Fore.YELLOW + 'CALCULO DE EXCESSO DE PESO'.center(30))
print(Fore.YELLOW + '*'*30)
peso = float(input('Peso dos peixes(Kg): '))

if peso > 50:
    excesso = peso - 50
    multa = 4 * excesso
    print(f'{Fore.RED}Voce está levando {excesso}Kg acima do peso permitido(50Kg)!')
    print(f'{Fore.RED}Voce terá que pagar uma multa de R${multa:.2f}')
else:
    print('Voce está levando a quantidade de acordo com o peso permitido')
print(Fore.GREEN + Style.BRIGHT + 'Tenha um bom dia!')