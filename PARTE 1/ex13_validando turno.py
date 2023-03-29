'''
Credito : https://wiki.python.org.br/EstruturaDeDecisao Ex10
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''
from os import system
system('cls')
print('Em qual turno voce estuda?')
turno = str(input('M-matutino | V-vespertino | N-noturno: ')).strip().upper()[0]
if turno in "M":
    print('BOM DIA!')
elif turno in "V":
    print('BOA TARDE!')
elif turno in "N":
    print('BOA NOITE!')
else:
    print("VALOR INVÁLIDO!")