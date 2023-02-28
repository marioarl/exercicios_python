'''
Credito : https://wiki.python.org.br/EstruturaSequencial
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool: até 20 litros, desconto de 3% por litro acima de 20 litros, desconto de 5% por litro
Gasolina: até 20 litros, desconto de 4% por litro acima de 20 litros, desconto de 6% por litro 

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 4,70 o preço do litro do álcool é R$ 3,70.
'''
from os import system
from colorama import init, Fore,Back,Style
init(autoreset= True)
print('-'*50)
print('POSTO TABAJARA'.center(50))
print('-'*50)
print(Fore.YELLOW + 'PREÇOS'.center(50))
print(f'{Fore.YELLOW}{"GASOLINA":.<30}R${"4,70"} p/ LITRO')
print(f'{Fore.YELLOW}{"ALCOOL":.<30}R${"3,70"} p/ LITRO')
litros = float(input('Quantidade de litros: '))
tipo = str(input('G - Gasolina\nA - Alcool \n>>> ')).strip().upper()[0]
if tipo in "G":
    total = 4.70 * litros
    if litros <=20:
        desconto = total * 4 / 100
        d = "4%"
    else:
        desconto = total * 6 / 100
        d = "6%"
elif tipo in "A":
    total = 3.70 * litros
    if litros <=20:
        desconto = total * 3 / 100
        d = "3%"
    else:
        desconto = total * 5 / 100
        d = "5%"
print(f'TOTAL: R${total:.2f}')
print(f'Desconto de {d}')
print(f'PREÇO FINAL: R${total - desconto:.2f}')