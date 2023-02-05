'''
Credito : https://wiki.python.org.br/EstruturaSequencial
Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo
'''

num = float(input('Digite um valor: '))
print(f'O numero {num} é ', end="")
if num < 0:
    print('NEGATIVO')
else:
    print('POSITIVO')