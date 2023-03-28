'''
Credito : https://wiki.python.org.br/EstruturaDeDecisao Ex4
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''
letra = str(input('Digite uma letra: ')).strip().upper()[0]
print(f'A letra {letra} é ', end="")
if letra in "AEIOU":
    print('VOGAL.')
else:
    print('CONSOANTE.')