''''
Credito : https://www.huicode.com.br/2020/09/ler-um-valor-inteiro-aceitar-somente.html ref: Ex1

Faça um programa que informe a versão do Python que você está utilizando.
'''
from colorama import Fore, init
init(autoreset=True)
import sys
print(f"Versao do Python {Fore.BLUE}{sys.version}")

print(f"Informação da versao instalada {sys.version_info}")