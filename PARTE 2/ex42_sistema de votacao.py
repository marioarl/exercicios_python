'''
Credito : https://wiki.python.org.br/EstruturaDeRepeticao Ex44

Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. 
Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. 
Para finalizar o conjunto de votos tem-se o valor zero.
'''
from os import system
from time import sleep
from colorama import init, Fore, Back
init(autoreset=True)
system('cls')
cand1 = cand2 = cand3 = cand4 = nulo = branco = totVotos = 0
while True:
    print(Back.RED + '='*50)
    print(Back.RED +'SISTEMA DE VOTAÇÃO - ETRURIA'.center(50))
    print(Back.RED +'='*50)
    print('[ 1 ] - Tarconte\n[ 2 ] - Publio Virgilio\n[ 3 ] - Herodoto\n[ 4 ] - Dionisio\n[ 5 ] - Voto Nulo\n[ 6 ] - Voto em Branco')
    while True:
        voto = int(input('>>> (Para encerrar aperte 0) '))
        if voto > 0 and voto <=6:
            break
        print(f'{Fore.RED}{"ERRO! Escolha somente as opções acima!"}')
    if voto == 1:
        cand1 += 1
    elif voto == 2:
        cand2 += 1
    elif voto == 3:
        cand3 += 1
    elif voto == 4:
        cand4 += 1
    elif voto == 5:
        nulo += 1
    elif voto == 6:
        branco += 1

    if voto == 0:
        break
    totVotos += 1
    print('VOTO CADASTRADO...')
    sleep(0.5)
    system('cls')
print(Fore.GREEN + '-='*20)
print(Fore.GREEN +'RESULTADO DA ELEIÇÃO'.center(40))
print(Fore.GREEN +'-='*20)
print(f'Tarconte........... {cand1}','votos' if cand1 > 1 else 'voto')
print(f'Publio Virgilio.... {cand2}','votos' if cand2 > 1 else 'voto')
print(f'Herodoto........... {cand3}','votos' if cand3 > 1 else 'voto')
print(f'Dionisio........... {cand4}','votos' if cand4 > 1 else 'voto')
print(f'Votos NULOS........ {nulo}','votos' if nulo > 1 else 'voto ', f'({(nulo/totVotos)*100:.1f}%)')
print(f'Votos em BRANCO.... {branco}','votos' if branco > 1 else 'voto ', f'({(branco/totVotos)*100:.1f}%)')
print('-'*40)
print(f'TOTAL...............{totVotos} votos')
    