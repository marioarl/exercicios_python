'''
Credito : https://wiki.python.org.br/EstruturaSequencial Ex18
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um 
link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link em minutos
'''

from colorama import Fore, init
init(autoreset=True)
tam = int(input('Innforme o tamanho do arquivo(em MB):  '))
velo = int(input('Informe a velocidade do link (em Mbps): '))
tempo = tam / (velo/8)
print(f'Tempo estimado para baixar um arquivo de {Fore.RED}{tam}MB\033[m com velocidade de {Fore.GREEN}{velo}Mbps\033[m: ', end="")
if tempo/60 < 1:
    print(Fore.BLUE+ 'Menos de 1 minuto...')
else:
    print(f'{Fore.YELLOW}{tempo/60:.0f} minutos\033[m')