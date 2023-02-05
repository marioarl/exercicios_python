'''
Credito : https://wiki.python.org.br/EstruturaSequencial
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
'''
prodA = float(input('Preço do Produto A: R$ '))
prodB = float(input('Preço do Produto B: R$ '))
prodC = float(input('Preço do Produto C: R$ '))

print('O produto mais barato é o ', end="")
if prodA < prodB < prodC:
    print('PRODUTO A')
elif prodB < prodC and prodB < prodA:
    print('PRODUTO B')
elif prodC < prodA and prodC < prodB:
    print('PRODUTO C')