'''
Credito : https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa
'''

listNum = []

for n in range(1,11):
    numero = int(input(f'Digite o {n}o. numero: '))
    listNum.append(numero)

print('Os numeros digitados na ordem inversa: ', end="")

cont = 0
for l in reversed(listNum):
    
    print(f'{l}', ', ' if cont <= 8 else '', end="")
    cont += 1