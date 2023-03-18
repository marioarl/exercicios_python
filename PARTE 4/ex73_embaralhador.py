'''
Credito : https://wiki.python.org.br/EstruturaSequencial ref: Ex funcoes 12

Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
'''
from os import system
from colorama import Fore, init
init(autoreset=True)
from random import shuffle
system('cls')


def embaralha(palavra):
    from random import shuffle
    lista= list(palavra)
    shuffle(lista)
    embaralhada = ''.join(lista)
    return embaralhada


palavra = str(input('Digite uma palavra: '))
print(f'A palavra que voce digitou foi embaralhada: {embaralha(palavra)}')

