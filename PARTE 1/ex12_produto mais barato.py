'''
Credito : https://wiki.python.org.br/EstruturaDeDecisao Ex8
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
'''
from colorama import Fore, init
init(autoreset=True)
prodA = float(input(Fore.YELLOW + 'Preço do Produto A: R$ ' + Fore.RESET))
prodB = float(input(Fore.RED + 'Preço do Produto B: R$ ' + Fore.RESET))
prodC = float(input(Fore.GREEN + 'Preço do Produto C: R$ ' + Fore.RESET))

print('O produto mais barato é o ', end="")
if prodA < prodB < prodC:
    print(Fore.YELLOW + 'PRODUTO A')
elif prodB < prodC and prodB < prodA:
    print(Fore.RED + 'PRODUTO B')
elif prodC < prodA and prodC < prodB:
    print(Fore.GREEN + 'PRODUTO C')