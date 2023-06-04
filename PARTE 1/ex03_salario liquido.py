'''
Credito : https://wiki.python.org.br/EstruturaSequencial Ex15
Faça um programa que pergunte quanto voce ganha por hora e o número de horas trabaçhadas no mes.
Calcule e mostre o total do seu salario no referido mes, sabendo-se que sao descontados 11% para 
o Imposto de Renda, 8% para o INSS e 5% para o sindicato e faça conforme abaixo:
a) salario bruto
b) quanto pagou ao INSS
c) quanto pagou ao sindicato
d) o salario liquido
e) calcule os descontos e o salário liquido
'''

from colorama import Fore, init, Back
init(autoreset=True)

qtyHoras = float(input('Quantidade de horas trabalhadas em 1 mes: '))
valorHora = float(input('Valor por Hora trabalhada: '))
sBruto = qtyHoras * valorHora
ir = sBruto * 11/100
inss = sBruto * 8 / 100
sind = sBruto * 5 / 100
descontos = ir + inss + sind
print(Back.GREEN + Fore.BLACK + '='*45)
print(Back.GREEN + Fore.BLACK + 'DEMONSTRATIVO DE PAGAMENTO'.center(45))
print(Back.GREEN + Fore.BLACK + '='*45)
print(f'{"+ Salário Bruto":.<30}', f'R${sBruto:>12.2f}')
print(f'{"- IR(11%)":.<30}', f'R${ir:>12.2f}')
print(f'{"- INSS(8%)":.<30}', f'R${inss:>12.2f}')
print(f'{"- Sindicato(5%)":.<30}', f'R${sind:>12.2f}')
print()
print(f'{"= Salário Liquido":.<30}', f'R${sBruto-descontos:>12.2f}')