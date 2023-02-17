'''
Credito : https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
'''

numeros = []
impar = []
par = []

for n in range(1,21):
    num = int(input(f'{n}o. numero: '))
    numeros.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f'Os numeros digitados foram: {numeros}')
print(f'Numeros PARES...: {par}')
print(f'Numeros IMPARES.: {impar}')
    

