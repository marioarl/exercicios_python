'''
Credito : https://wiki.python.org.br/EstruturaDeDecisao Ex28
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o 
cliente receberá ainda um desconto de 5% sobre o total da compra, dinheiro 10% de desconto, outros cartoes preço normal 
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
contendo as informações da compra: 
tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
'''
print('-='*30)
print('HIPERMARCADO TABAJARA'.center(60))
print('-='*30)
print('[ F ] - File duplo\n[ A ] - Alcatra\n[ P ] - Picanha')
while True:
    tipo = str(input('Tipo da carne: ')).strip().upper()[0]
    if tipo in "FAP":
        break
qtd = float(input('Quantidade (Kg): '))
if tipo in "F":
    nom = "File Duplo"
    if qtd <=5:
        preco = 37.90
    else:
        preco = 35.00
elif tipo in "A":
    nom = "Alcatra"
    if qtd <=5:
        preco = 44.90
    else:
        preco = 42.90

elif tipo in "P":
    nom = "Picanha"
    if qtd <= 5:
        preco = 69.90
    else:
        preco = 67.90

total = preco * qtd
desconto = 0
print('Qual a forma de pagamento? ')
print('[ 1 ] - Cartão TABAJARA (desconto de 5%)\n[ 2 ] - Dinheiro (desconto de 10%)\n[ 3 ] - Outros Cartões (Preço normal)')
while True:
    pag = int(input('>>> '))
    if pag > 0 and pag <=3:
        break
    print('\033[31mERRO!Digite as opções F, A ou P\033[m')
if pag == 1:
    nomPag = 'Cartão Tabajara'
    desconto = total * 5 / 100
elif pag == 2:
    nomPag = 'Dinheiro'
    desconto = total * 10 / 100
elif pag == 3:
    nomPag = 'Outros Cartões'
    desconto = 0
print('*'*20 ,f'{"CUPOM FISCAL"}', '*'*20)
print('ORGANIZAÇÕES TABAJARA'.center(52))
print('PO MAJÉ'.center(52))
print('RUA APOLINARIO SALVATORE, 1220'.center(52))
print('JD. ITUANO - RIO DE JANEIRO - RJ'.center(52))
print('CNPJ - 45.678.322/2290-89'.center(52))
print('.'*52)
print(f'{"Descrição do Produto":<30}{"Qtd":>20}')
print('.'*52)
print(f'{nom:<30}{qtd:>20}Kg')
print()
print(f'{"Preço Total R$":<30}{total:>22.2f}')
print(f'{"Tipo de pagamento":<30}{nomPag:>22}')
print(f'{"Valor do desconto R$":<30}{desconto:>22.2f}')
print(f'{"VALOR A PAGAR R$":<30}{total-desconto:>22.2f}')
print()
print('*'*52)