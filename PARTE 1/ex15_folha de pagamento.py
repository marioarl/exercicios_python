'''
Credito : https://wiki.python.org.br/EstruturaDeDecisao Ex12
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e que o FGTS corresponde a 11% 
do Salário Bruto, mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor
da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% 
Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
Salário Bruto: (5 * 220)        : R$ 1100,00
(-) IR (5%)                     : R$   55,00  
(-) INSS ( 10%)                 : R$  110,00
FGTS (11%)                      : R$  121,00
Total de descontos              : R$  165,00
Salário Liquido                 : R$  935,00
'''

qtyHoras = float(input('Quantidade de horas trabalhadas em 1 mes: '))
valorHora = float(input('Valor por Hora trabalhada: '))
sBruto = qtyHoras * valorHora
if sBruto <= 900:
    ir = 0
    tipo = "ISENTO"
elif sBruto >900 and sBruto <=1500:
    ir = sBruto * 5 / 100
    tipo = "5%"
elif sBruto > 1500 and sBruto <= 2500:
    ir = sBruto * 10 / 100
    tipo = "10%"
elif sBruto > 2500:
    ir = sBruto * 20 / 100
    tipo = "20%"

inss = sBruto * 10 / 100
fgts = sBruto * 11 / 100
descontos = inss + ir
print('='*55)
print('DEMONSTRATIVO DE PAGAMENTO'.center(55))
print('='*55)
print(f'Salário Bruto: ({valorHora:.0f} * {qtyHoras:.0f})\t\t: R$ {sBruto:.2f}')
print(f'(-) IR ({tipo})\t\t\t\t: R$ {ir:.2f}')
print(f'{"(-) INSS (10%)"}\t\t\t\t: R$ 'f'{inss:.2f}')
print(f'{"FGTS (11%)":<39} : R$ {fgts:.2f}')
print(f'{"Total de descontos":<39} : R$ {descontos:.2f}')
print(f'{"Salário Liquido":<39} : R$ {sBruto - descontos:.2f}')

