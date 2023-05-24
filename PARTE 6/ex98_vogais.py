'''
Contagem de vogais
Escreva um programa que recebe uma palavra do usuário e conte a quantidade de vogais presentes nessa palavra. Este programa deve rodar até que o usuario digite a palavra sair.
Utilize um loop `for` para percorrer cada letra da palavra e um loop `while` para solicitar a entrada até que uma palavra seja digitada.'''

while True:
    cont = 0
    palavra = str(input('Digite uma palavra (ou "sair" para encerrar): ')).strip().upper()
    if palavra in "SAIR":
        break
    for p in palavra:
        if p in "AEIOU":
            cont += 1
    print(f'A palavra {palavra} possui {cont} vogais')
print('Programa encerrado')