'''
Credito : https://wiki.python.org.br/EstruturaSequencial ref: Ex listas 24

Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.

'''
from os import system
from random import randint
from collections import Counter

system('cls')
def aleatorio(ini, fim):
    x = randint(ini,fim)
    return x

resultados = []

for i in range(100):
    resultados.append(aleatorio(1,6))

resultados.sort()

contagem = Counter(resultados)

print('RESULTADO DOS DADOS')
print('===================')
for n, q in contagem.items():
    print(f'O número {n} foi sorteado {q} vezes.')



