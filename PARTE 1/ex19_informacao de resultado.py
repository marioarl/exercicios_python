'''
Credito : https://wiki.python.org.br/EstruturaDeDecisao Ex24
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
 - par ou ímpar;
 - positivo ou negativo;
 - inteiro ou decimal.
'''

from colorama import Fore
from os import system
system('cls')
n1 = float(input('Digite o 1o. numero: '))
n2 = float(input('Digite o 2o. numero: '))
res = 0
print(Fore.BLUE + "1 \033[m- Somar")
print(Fore.YELLOW + "2 \033[m - Subtrair")
print(Fore.GREEN + "3 \033[m - Dividir")
print(Fore.MAGENTA + "4 \033[m - Multiplicar")
while True:
    op = str(input('Qual operação deseja realizar? ')).strip()[0]
    if op in "1234":
        break
if op == "1":
    res = n1 + n2
    print(f'A soma entre {n1} e {n2} = {res}')
elif op == "2":
    res = n1 - n2
    print(f'A {Fore.YELLOW}subtração\033[m entre {n1} e {n2} = {res}')
elif op == "3":
    res = n1 / n2
    print(f'A {Fore.GREEN}divisão\033[m entre {n1} e {n2} = {res:.2f}')
elif op == "4":
    res = n1 * n2
    print(f'A {Fore.MAGENTA}multiplicação\033[m entre {n1} e {n2} = {res}')
print(f'O resultado da operação indica que o numero é ', end="")
if res % 2 == 0:
    print('PAR, ', end="")
else:
    print('IMPAR, ', end="")
if res > 0:
    print('POSITIVO, ', end="")
else:
    print("NEGATIVO, ",end="")
if res == round(res):
    print('INTEIRO')
else:
    print('DECIMAL')