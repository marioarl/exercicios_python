'''
Credito : https://wiki.python.org.br/EstruturaDeDecisao Ex2
Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo
'''

num = float(input('Digite um valor: '))
print(f'O número {num} é ', end="")
if num < 0:
    print('NEGATIVO')
else:
    print('POSITIVO')