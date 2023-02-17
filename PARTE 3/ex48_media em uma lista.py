'''
Credito : https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''

notas = []
somaNotas = 0
for n in range(1,5):
    nt = float(input(f'Digite a {n}a. nota: '))
    notas.append(nt)
    somaNotas += nt
media = somaNotas / 4

print(f'As notas foram: {notas}')
print(f'Média.........: {media:.2f} ')