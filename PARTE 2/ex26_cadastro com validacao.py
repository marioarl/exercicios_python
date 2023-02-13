'''
Credito : https://wiki.python.org.br/EstruturaSequencial
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''
print('='*30)
print('SISTEMA DE CADASTRO'.center(30))
print('='*30)
while True:
    nome = str(input('Nome: '))
    if len(nome) > 3:
        break
    print('\033[31mERRO!! Nome deve ter mais de 3 caracteres\033[m')
while True:
    try:
        idade = int(input('Idade:'))
    except ValueError:
        print('\033[31mERRO!Campo deve ser preenchido\033[m')
        continue
    if idade >=0 and idade <=150:
        break
    print('\033[31mERRO" Idade de ser entre 0 e 150\033[m')

while True:
    try:
        salario = float(input('Salário R$: '))     
    except ValueError:
        print("\033[31mERRO! Campo salario deve ser preenchido\033[m")
        continue
    if salario > 0:
            break
    print('ERRO! Salario deve ser maior que 0')

while True:    
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if sexo in "MF":
        break
    print('ERRO! Digite apenas M ou F')

while True:
    estadoC = str(input('Estado Civil\n[ S ] - Solteiro(a) \n[ C ] - Casado(a)\n[ V ] - Viuvo(a)\n[ D ] - Divorciado(a)\n>>> ')).upper().strip()[0]
    if estadoC in 'SCVD':
        break
    print('ERRO! Digite apenas "S", "C", "V", "D"')
print(f'As informações digitadas foram:')
print(f'{"Nome":<20}{"Idade":<5}{"Salário":>12}{"Sexo":>8}{"Estado Civil":>15}')
print('-'*60)
print(f'{nome:<20}{idade:>5}{salario:>12.2f}{sexo:>8}{estadoC:>9}')
print()