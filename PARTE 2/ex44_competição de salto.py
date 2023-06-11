'''
Credito : https://wiki.python.org.br/EstruturaDeRepeticao Ex46

Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m
'''

from os import system
from time import sleep
system('cls')
while True:
    atleta = str(input('Nome do atleta: ')).strip()
    if atleta == "":
        break
    ordemSaltos = ('Primeiro Salto', 'Segundo Salto', 'Terceiro Salto', 'Quarto Salto', 'Quinto Salto')
    saltos = []
    somaSaltos = media = 0
    for s in range(0,5):
        salto = float(input(f'{ordemSaltos[s]}: '))
        somaSaltos += salto
        saltos.append(salto)
    system('cls')
    media = ((somaSaltos-(max(saltos)+min(saltos)))/3)
    print('='*50)
    print('COMPETIÇÃO DE SALTO'.center(50))
    print('='*50)
    print(f'Atleta: {atleta}')
    print('-'*50)
    for s in range(0,5):
        print(f'{ordemSaltos[s]:<18}:{saltos[s]:>5}m')
    print('-'*50)
    print(f'Melhor Salto:          : {max(saltos)}','m')
    print(f'Pior Salto:            : {min(saltos)}','m')
    print(f'Média dos demais saltos: {media:.1f}', 'm')
    print('='*16 , ' RESULTADO FINAL ', '='*16)
    print(f'{atleta}: {media:.1f}m')
    sleep(3)
    system('cls')

print('FIM')