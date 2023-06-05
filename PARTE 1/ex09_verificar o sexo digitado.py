'''
Credito : https://wiki.python.org.br/EstruturaDeDecisao Ex3
Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

from colorama import Fore, init
init(autoreset=True)

sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
print('Voce digitou o sexo ', end='')
if sexo in "M":
    print(Fore.BLUE + 'Masculino')
elif sexo in "F":
    print(Fore.MAGENTA + 'Feminino')
else:
    print('Sexo Inválido')