'''
Credito : https://wiki.python.org.br/EstruturaDeRepeticao Ex43

O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor 
a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar 
quando o pedido deve ser encerrado.
'''
from os import system
from colorama import Fore, Back, Style, init
init(autoreset=True)
system('cls')
pedido = 1 #numero do pedido
totalDia = 0 # total vendido em um dia
listaP = []
temp = {}
while True:
    listaP.clear()
    temp.clear()
    total = 0 #total do pedido
    system('cls')
    print(Back.WHITE + '='*50)
    print(Back.WHITE +'LANCHONETE LARICA (CARDÁPIO)'.center(50))
    print(f'{Back.WHITE}{"Especificação":<18}{"Código":<6}{"Preco":>8}{"":>18}')
    print(f'{Back.WHITE}{"Cachorro Quente":<18}{"100":<6}{"R$ 1,20":>10}{"":>16}')
    print(f'{Back.WHITE}{"Bauru Simples":<18}{"101":<6}{"R$ 1,30":>10}{"":>16}')
    print(f'{Back.WHITE}{"Bauru com ovo":<18}{"102":<6}{"R$ 1,50":>10}{"":>16}')
    print(f'{Back.WHITE}{"Hamburguer":<18}{"103":<6}{"R$ 1,20":>10}{"":>16}')
    print(f'{Back.WHITE}{"Cheeseburguer":<18}{"104":<6}{"R$ 1,30":>10}{"":>16}')
    print(f'{Back.WHITE}{"Refrigerante":<18}{"105":<6}{"R$ 1,00":>10}{"":>16}')
    print(Back.WHITE + '='*50)
    print(f'Pedido No. {pedido}')
    while True:
        print('.'*50)
        temp['codigo'] = int(input('Código do produto: '))
        if temp['codigo'] == 100:
            temp['esp'] = "Cachorro Quente"
            temp['preco'] = 1.20
        elif temp['codigo'] == 101:
            temp['esp'] = "Bauru Simples"
            temp['preco'] = 1.30
        elif temp['codigo'] == 102:
            temp['esp'] = "Bauru com ovo"
            temp['preco'] = 1.50
        elif temp['codigo'] == 103:
            temp['esp'] = "Hamburguer"
            temp['preco'] = 1.20
        elif temp['codigo'] == 104:
            temp['esp'] = "Cheeseburguer"
            temp['preco'] = 1.30
        elif temp['codigo'] == 105:
            temp['esp'] = "Refrigerante"
            temp['preco'] = 1.00
        temp['qtd'] = int(input('Quantidade: '))
        temp['sub'] = temp['qtd'] * temp['preco']
        total += temp['sub']
        totalDia += total
        listaP.append(temp.copy())
        op = str(input('Continua? [S/N] ')).strip().upper()[0]
        if op in "N":
            break
        
    print('='*14, f'RESUMO DO PEDIDO No.{pedido}', '='*14)
    print(f'{"Item":<3}{"Especificação":>15}{"Qtd":>8}{"Preço":>8}{"Subtotal":>15}')
    for i, p in enumerate(listaP):
        print(f'0{i+1:<5}{p["esp"]:<15}{p["qtd"]:>5}{p["preco"]:>8.2f}{p["sub"]:>15.2f}')
    print(f'\nTOTAL DO PEDIDO: R${total:.2f}')
    print('='*50)
    proximo = str(input('Próximo pedido? [S/N]: ')).strip().upper()[0]
    pedido += 1 
    if proximo in "N":
        break   

print()
print('OBRIGADO POR UTILIZAR O PROGRAMA')
print(f'Total de pedidos:.....{pedido -1}')
print(f'Valor total do dia:...R$ {totalDia:.2f}')