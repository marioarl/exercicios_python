''''
Credito : https://www.huicode.com.br/2020/09/ler-um-valor-inteiro-aceitar-somente.html ref: Ex6

Escreva um programa que mostre todos os números entre 5 e 100 que são divisíveis por 7, mas não são múltiplos de 5. 
Os números obtidos devem ser impressos em sequência.
'''
from colorama import Fore, init
init()
for num in range(5, 100):
    if (num % 7 == 0 and num % 5 != 0):
        print(f"{num}", end=" ")
print()