'''
Credito : https://wiki.python.org.br/EstruturaSequencial
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
print(Fore.BLUE + "1 \033[m- Somar\n2 - Subtrair\n3 - Dividir\n4 - Multiplicar")
print(Fore.YELLOW + "2 \033[m - Subtrair")
print(Fore.GREEN + "3 \033[m - Dividir")
while True:
    op = str(input('Qual operação deseja realizar? ')).strip()[0]
    if op in "1234":
        break
if op == "1":
    res = n1 + n2
    print(f'A soma entre {n1} e {n2} = {res}')
elif op == "2":
    res = n1 - n2
    print(f'A subtração entre {n1} e {n2} = {res}')
elif op == "3":
    res = n1 / n2
    print(f'A divisão entre {n1} e {n2} = {res}')
elif op == "4":
    res = n1 * n2
    print(f'A multiplicação entre {n1} e {n2} = {res}')
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