'''
Credito : https://wiki.python.org.br/EstruturaSequencial
Faça um programa que peça 5 numeros e imprima qual é o maior e o menor
'''

# Opção 1 => Utilizando as funcoes max(para achar o maior numero) e min(para o menor numero) e
# colocando os numeros em uma lista
numeros = []
for n in range(1,6):
    numeros.append(int(input(f'Digite o {n}o. numero: ')))
print(f'Os numeros digitados foram: {numeros}')
print(f'Numero maior: {max(numeros)}')
print(f'Numero menor: {min(numeros)}')

#opção 2 => Utilizando variaveis maior e menor
maior = menor = 0
for n in range(1,6):
    num = int(input(f'Digite o {n}o. numero: '))
    if n == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'Numero maior: {maior}')
print(f'Numero menor: {menor}')



