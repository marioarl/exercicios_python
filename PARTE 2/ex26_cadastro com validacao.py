'''
Credito : https://wiki.python.org.br/EstruturaDeRepeticao Ex3
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''

from colorama import Fore,init
init(autoreset=True)

print('='*30)
print('SISTEMA DE CADASTRO'.center(30))
print('='*30)
while True:
    nome = str(input('Nome: '))
    if len(nome) > 3:
        break
    print(Fore.RED + 'ERRO!! Nome deve ter mais de 3 caracteres')
while True:
    try:
        idade = int(input('Idade:'))
    except ValueError:
        print(Fore.RED + 'ERRO!Campo deve ser preenchido')
        continue
    if idade >=0 and idade <=150:
        break
    print(Fore.RED + 'ERRO! Idade de ser entre 0 e 150')

while True:
    try:
        salario = float(input('Salário R$: '))     
    except ValueError:
        print(Fore.RED + "ERRO! Campo salario deve ser preenchido")
        continue
    if salario > 0:
            break
    print(Fore.RED + 'ERRO! Salario deve ser maior que 0')

while True:
    try:   
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    except IndexError:
        print(Fore.RED + "ERRO! Campo salario deve ser preenchido")
        continue
    if sexo in "MF":
        break
    print(Fore.RED + 'ERRO! Digite apenas M ou F')

while True:
    try:
        estadoC = str(input('Estado Civil\n[ S ] - Solteiro(a) \n[ C ] - Casado(a)\n[ V ] - Viuvo(a)\n[ D ] - Divorciado(a)\n>>> ')).upper().strip()[0]
    except IndexError:
        print(Fore.RED + "ERRO! Campo salario deve ser preenchido")
        continue
    if estadoC in 'SCVD':
        break
    print(Fore.RED + 'ERRO! Digite apenas "S", "C", "V", "D"')
print(f'As informações digitadas foram:')
print(f'{"Nome":<25}{"Idade":<5}{"Salário":>12}{"Sexo":>8}{"Estado Civil":>15}')
print('-'*65)
print(f'{nome:<25}{idade:>5}{salario:>12.2f}{sexo:>8}{estadoC:>9}')
print()