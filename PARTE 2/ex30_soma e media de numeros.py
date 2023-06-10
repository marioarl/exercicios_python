'''
Credito : https://wiki.python.org.br/EstruturaDeRepeticao Ex8
Faça um programa que leia 5 números e informe a soma e a média dos números
'''

media = soma = 0

for n in range(1,6):
    num = int(input(f'Digite o {n}o. numero: '))
    soma += num
media = soma / 5
print(f'A soma dos valores digitados é: {soma}')
print(f'A média dos valores digitados é : {media:.2f}')