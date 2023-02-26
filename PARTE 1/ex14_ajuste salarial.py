'''
Credito : https://wiki.python.org.br/EstruturaSequencial
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para 
desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
baseado no salário atual:
 - salários até R$ 280,00 (incluindo) : aumento de 20%
 - salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
 - salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
 - salários de R$ 1500,00 em diante : aumento de 5% 

Após o aumento ser realizado, informe na tela:
 - salário antes do reajuste;
 - percentual de aumento aplicado;
 - valor do aumento;
 - novo salário, após o aumento.

'''
from colorama import Fore, init
init(autoreset=True)
aumento = 0
perc = ""
salario = float(input('Informe o valor do salário: R$'))
if salario <= 280:
    aumento = salario * 20 / 100
    perc = "20%"
elif salario > 280 and salario <= 700:
    aumento = salario * 15 / 100
    perc = "15%"
elif salario > 700 and salario <= 1500:
    aumento = salario * 10 / 100
    perc = "10%"
else:
    aumento = salario * 5 / 100
    perc = "5%"
print('='*50)
print('RESUMO'.center(50))
print('='*50)
print(f'{"Salário antes do reajuste":.<40}' f'R${salario:.2f}')
print(f'{"Percentual de aumento aplicado":.<40}' f'{perc}')
print(f'{"Valor do aumento":.<40}' f'R${aumento:.2f}')
print(Fore.YELLOW + "*"*50)
print(f'{Fore.YELLOW}{"* Novo salário após aumento":.<40}' f'R${salario + aumento:.2f} *')
print(Fore.YELLOW + "*"*50)