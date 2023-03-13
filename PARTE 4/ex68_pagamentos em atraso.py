'''
Credito : https://wiki.python.org.br/EstruturaSequencial ref: Ex funcoes 7

Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. 
Após a execução, o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. 
O cálculo do valor a ser pago é feito da seguinte forma: 
Para pagamentos sem atraso, cobrar o valor da prestação, quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.    
'''
from os import system
from time import sleep
from colorama import Fore, init
init(autoreset=True)
tot = []
system('cls')

def valorPagamento(valor, dias):
    if dias == 0:
        v = valor
    else:
        multa = valor * 3 / 100
        mDias = (valor * 0.1 / 100) * dias
        v = valor + multa + mDias
    return v

while True:
    valor = float(input('Valor da prestação: R$ '))
    if valor == 0:
        print('PROGRAMA ENCERRADO')
        break
    d = int(input('Quantos dias atrasado: '))
    tot.append(valorPagamento(valor,d))
    print(f'Valor a ser pago com multa de 3% e 0.1% de juros ao dia: R$ {valorPagamento(valor,d):.2f}')
    sleep(2)
    system('cls')

print('===== RELATORIO DIÁRIO =====')
print(f'Quatidade de prestações pagas.....: {len(tot)}')
print(f'Valor total das prestações pagas..: R$ {sum(tot):.2f}')
    
