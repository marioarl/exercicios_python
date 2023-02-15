'''
Credito : https://wiki.python.org.br/EstruturaSequencial
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro
'''
from colorama import init, Fore
init(autoreset=True)
print('Os numeros de 1 a 20 um abaixo do outro:')
for n in range(1,21):
    print(n)

print(Fore.CYAN + 'Agora um ao lado do outro:')
for n in range(1,21):
    print(f'{Fore.GREEN}{n} ', end="")