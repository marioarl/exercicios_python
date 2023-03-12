'''
Credito : https://wiki.python.org.br/EstruturaSequencial ref: Ex funcoes 6

Faça um programa que converta da notação de 24 horas para a notação de 12 horas. 
Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. 
Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. 
Registre a informação A.M./P.M. como um valor A para A.M. e P para P.M. 
Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
'''
from os import system
from colorama import Fore, init
init(autoreset=True)
system('cls')

def convHora(h,m):
    if h == 0:
        horario = 12
        periodo = 'A'
    elif h < 12:
        horario = h
        periodo = 'A'
    elif h  == 12:
        horario = 12
        periodo = 'P'
    else:
        horario = h -12
        periodo = 'P'
    return horario, m, periodo

def imprime_horario(horario):
    print(f'{Fore.CYAN}{horario[0]}:{horario[1]}  {horario[2]}.M.')

while True:
    h = int(input('Digite a hora (0-23): '))
    m = int(input('Digite os minutos (0-59):'))

    horario_convertido = convHora(h,m)
    print(Fore.YELLOW + 'HORARIO CONVERTIDO')
    imprime_horario(horario_convertido)

    while True:
        op = str(input('Deseja converter outro horario? (S/N) ')).strip().upper()
        if op in 'SN':
            break
    system('cls')
    if op == 'N':
        break


