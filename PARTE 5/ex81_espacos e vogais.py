'''
Credito : https://wiki.python.org.br/EstruturaSequencial ref: Ex Com Strings 7

Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.
'''
from os import system
system('cls')

frase = str(input('Digite uma frase: ')).strip().upper()

print(f'Espaços em branco: {frase.count(" ")}')
print(f'Vogal A: {frase.count("A")}')
print(f'Vogal E: {frase.count("E")}')
print(f'Vogal I: {frase.count("I")}')
print(f'Vogal O: {frase.count("O")}')
print(f'Vogal U: {frase.count("U")}')
    


