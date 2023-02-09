'''
Credito : https://wiki.python.org.br/EstruturaSequencial
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
'''
from os import system
voto1 = voto2 = voto3 = 0
candidato1 = "Toninho do Gas"
candidato2 = "Denilson Chulé"
candidato3 = "Andreson Sucatão"
print('='*50)
print('SISTEMA ELEITORAL DA CIDADE DE RIO DOS CANTOS')
print('='*50)
numEleitores = int(input('Quantidade de eleitores: '))
system('cls')

for e in range(1, numEleitores+ 1):
    print('='*50)
    print('SISTEMA ELEITORAL DA CIDADE DE RIO DOS CANTOS')
    print('='*50)
    print(f'Escolha o candidato abaixo \033[31mELEITOR {e}\033[m:\n[ 1 ] - Toninho do Gas\n[ 2 ] - Denilson Chulé\n[ 3 ] - Anderson Sucatão')
    voto = int(input('>>> '))
    if voto == 1:
        voto1 += 1
    elif voto == 2:   
        voto2 += 1
    elif voto == 3:
        voto3 += 1
    system('cls')
print('-='*25)
print('RESULTADO DA ELEIÇÃO'.center(50))
print('-='*25)
print(f'{"Candidato":<25}{"Qtd":>14}{"%":>9}')
print(f'{"Votos":>41}')
print('-'*50)
print(f'{candidato1:.<35}{" "}{voto1:<10}{(voto1 / numEleitores)*100:.1f}')
print(f'{candidato2:.<35}{" "}{voto2:<10}{(voto2 / numEleitores)*100:.1f}')
print(f'{candidato3:.<35}{" "}{voto3:<10}{(voto3 / numEleitores)*100:.1f}')
print()
print('='*50)
print(f'\033[31mFIM DA ELEIÇÃO\033[m'.center(58))
print('='*50)


