'''
Credito : https://wiki.python.org.br/ExerciciosComStrings ref: Ex Com Strings 6

Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.
'''

from os import system
from colorama import Fore, init
init(autoreset=True)
system('cls')

dia = int(input('Dia: '))
mes = int(input('Mes: '))
ano = int(input('Ano: '))

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

print(f'Voce nasceu em {Fore.BLUE}{dia} de {Fore.YELLOW}{meses[mes-1]} de {Fore.GREEN}{ano}')
    


