'''
Credito : https://wiki.python.org.br/EstruturaDeRepeticao Ex47

Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
'''

from os import system
somaNotas = 0
atleta = str(input('Nome do Atleta: ')).strip()
notas = []
for n in range(1,8):
    nota = float(input(f'Nota Jurado {n}: '))
    notas.append(nota)
    somaNotas += nota

melhor = max(notas)
pior = min(notas)
media = (somaNotas - (melhor + pior)) / 5


print(f'Atleta: {atleta}')
for n in notas:
    print(f'Nota: {n}')
print('Resultado final')
print(f'Melhor nota: {melhor:.1f}')
print(f'Pior nota..: {pior:.1f}')
print(f'Média......: {media:.2f}')

