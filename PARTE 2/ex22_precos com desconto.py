'''
Credito : https://wiki.python.org.br/EstruturaSequencial
Uma quitanda está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda 
um desconto de 10% sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e 
escreva o valor a ser pago pelo cliente.
'''
from os import system
from colorama import Back, Fore, init
init(autoreset=True)
print('-='*30)
print('QUITANDA DO MANÉ'.center(60))
print('-='*30)
morango = float(input('Peso dos morangos (kg): '))
maca = float(input('Peso das maças (kg): '))
if morango <=5:
    preco1 = 2.50
else:
    preco1 = 2.20
if maca <=5:
    preco2 = 1.80
else:
    preco2 = 1.50
subTotal1 = preco1 * morango
subTotal2 = preco2 * maca
total = subTotal1 + subTotal2


print('-'*50)
print(f'{"Produto":<20}{"Qtd(Kg)":<10}{"Preço(R$)":<10}{"Total(R$)":<10}')
print('-'*50)
print(f'{"Morango":<20}{morango:<10.2f}{preco1:>8.2f}{subTotal1:>10.2f}')
print(f'{"Maça":<20}{maca:<10.2f}{preco2:>8.2f}{subTotal2:>10.2f}')
print(f'{Fore.RED}{"SUBTOTAL":<20}{subTotal1+subTotal2:>28.2f}')
print('-'*50)
if morango + maca > 8 or total > 25:
    desconto = total * 10 /  100
    print(f'{Fore.YELLOW}{"TOTAL DAS COMPRAS COM 10% de desconto"}{"":>6}{(subTotal1+subTotal2) - (desconto):.2f}')
else:
    print(f'{Fore.YELLOW}{"TOTAL DAS COMPRAS":<44}{subTotal1+subTotal2:.2f}\033[m')
