'''
Credito : https://wiki.python.org.br/EstruturaSequencial
Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
'''

num = int(input('Digite um numero: '))
print(f'O numero {num} digitado é ', end="")
if num % 2 == 0:
    print("PAR")
else:
    print("IMPAR")