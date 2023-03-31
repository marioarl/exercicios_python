'''
Credito :https://wiki.python.org.br/EstruturaDeRepeticao Ex14
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
'''
pares = impares = 0
for n in range(1,11):
    num = int(input(f'Digite o {n}o. numero: '))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f'Quantidade de numeros PARES:   {pares}')
print(f'Quantidade de numeros IMPARES: {impares}')