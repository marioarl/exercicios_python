'''
Credito : https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
'''

alpha = []
consoante = 0
for l in range(1,11):
    letra = str(input(f'Digite a {l}a. letra: ')).strip().upper()[0]
    if letra not in "AEIOU":
        consoante += 1
        alpha.append(letra)
print(f'Foram lidas {consoante} consoantes')
print(f'As consoantes foram {alpha}')