'''
Credito : https://wiki.python.org.br/EstruturaDeRepeticao Ex5
Faça um programa que o usuario digite o nome de 2 Paises (A e B), a população de dois paises e suas taxas de crescimento, 
mostre o resultado de quantos anos o pais A se iguale ou ultrapasse o pais B na quantidade de população. E tambem que 
o programa encerre quando o usuario informar NÃO em continuar.
OBS: O programa deverá ser capaz de identificar se a populacao do pais A é maior que a do país B e 
efetue os calculos corretos
'''
from colorama import init, Fore
init(autoreset=True)
from os import system
from time import sleep
while True:
    system('cls')
    print('-='*40)
    print('TAXA POPULACIONAL'.center(80))
    print('-='*40)
    while True:
        paisA = str(input('Nome do país A: ')).strip()
        if paisA.isalpha():
            break
        print(Fore.RED + 'ERRO! Este campo deverá ter apenas LETRAS')      
    popA = int(input(f'População do pais {paisA}: '))
    taxaA = float(input(f'Taxa de crescimento do pais {paisA} (%): '))
    print('.'*80)
    
    while True:
        paisB = str(input('Nome do país B: ')).strip()
        if paisB.isalpha():
            break
        print(Fore.RED + 'ERRO! Este campo deverá ter apenas LETRAS')
    popB = int(input(f'População do pais {paisB}: '))
    taxaB = float(input(f'Taxa de crescimento do pais {paisB} (%): '))
    anos = 0
    while True:
        if popA > popB:
            popA += popA * taxaA / 100
            popB += popB * taxaB / 100
            anos += 1
            if popB >= popA:
                print('='*80)
                print(f'{paisB} levará {anos} anos para que se iguale ou supere a população do país {paisA}')
                print('='*80)
                break
        elif popB > popA:
            popA += popA * taxaA / 100
            popB += popB * taxaB / 100
            anos += 1
            if popA >= popB:
                print('='*80)
                print(f'{paisA} levará {anos} anos para que se iguale ou supere a população do país {paisB}')
                print('='*80)
                break
    while True:
        op = str(input('\nContinuar? [S/N]: ')).strip().upper()[0]
        if op in "SN":
            break
        print(Fore.RED + 'ERRO! Digite apenas S ou N')
    if op in "N":
        print('FINALIZANDO...')
        sleep(1.5)
        break
print('OBRIGADO POR USAR O PROGRAMA! VOLTE SEMPRE!')