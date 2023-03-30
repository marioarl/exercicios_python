'''
Credito : https://wiki.python.org.br/EstruturaDeRepeticao Ex1
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido
e continue pedindo até que o usuário informe um valor válido.
'''
from colorama import Fore, init
init(autoreset=True)
while True:
    nota = int(input('Digite uma nota entre 0 e 10: '))
    if nota <0 or nota >10:
        print(Fore.RED + 'Valor Invalido!! ', end="")
    
    if nota >0 and nota <=10:
        break
print(f'A nota digitada foi {nota}')