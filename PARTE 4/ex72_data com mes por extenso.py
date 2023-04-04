'''
Credito : https://wiki.python.org.br/ExerciciosFuncoes ref: Ex funcoes 11

Data com mês por extenso. 
Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
'''
from os import system
from colorama import Fore, init
init(autoreset=True)
system('cls')


def valida_data(dia, mes, ano):
    mes_extenso = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto',
       'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    #Verificando se o dia mes e ano foram digitados corretos
    if dia >31 or dia < 0 or mes < 1 or mes > 12 or ano < 1:
        valido1 = False
    else:
        valido1 = True
    
    #Verificando se os meses estao com os dias corretos
    
    #Se os meses de janeiro,março,maio,julho,agosto,outubro e dezembro tem 31 dias
    if mes in [1,3,5,7,8,10,12] and dia<=31:   
        valido2 = True
    #Se o mes de fevereiro tem 29 dias (ANo bissexto nao conta)
    elif mes in [2] and dia <=29:
        valido2 = True
    elif mes in [2] and dia > 28:
        valido2 = False
    
    #Se os meses de abril, junho, setembro e novembro tem 30 dias
    elif mes in [4,6,9,11] and dia <31:
        valido2 = True
    elif mes in [4,6,9,11] and dia >=31:
        valido2 = False
    #Verifica se os validadores estao em TRUE
    if valido1 and valido2:
        print(f'{Fore.CYAN}Data por extenso: {dia:02d} de {mes_extenso[m-1]} de {ano}')   
    else:
        print(Fore.RED + 'DATA INVÁLIDA')
    


d = int(input('Dia: '))
m = int(input('Mes: '))
a = int(input('ano: '))

valida_data(d,m,a)