'''
Credito : https://wiki.python.org.br/EstruturaSequencial
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
'''
from colorama import init, Fore
init(autoreset=True)
temperaturas = []
while True:
    temperaturas.append(float(input('Digite a temperatura em graus Celcius: ')))
    while True:
        cont = str(input('Continuar [S/N] ')).strip().upper()[0]
        if cont in "SN":
            break
        print(Fore.RED + 'ERRO, Digite apenas S ou N')
    if cont in "N":
        break
print(f'A MAIOR temperatura digitada foi {max(temperaturas)} graus')
print(f'A MENOR temperatura digitada foi {min(temperaturas)} graus')
print(f'A MÉDIA das temperaturas é {sum(temperaturas)/ len(temperaturas):.1f} graus')