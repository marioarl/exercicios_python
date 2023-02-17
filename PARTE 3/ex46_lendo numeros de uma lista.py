'''
Credito : https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
'''

listNum = []

for n in range(1,6):
    numero = int(input(f'Digite o {n}o. numero: '))
    listNum.append(numero)

print('Os numeros digitados foram: ', end="")

cont = 0
for l in listNum:
    
    print(f'{l}', ', ' if cont <= 3 else '', end="")
    cont += 1