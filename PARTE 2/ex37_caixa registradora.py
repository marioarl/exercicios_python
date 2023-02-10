'''
Credito : https://wiki.python.org.br/EstruturaSequencial
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. 
Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de 
valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da
compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então
calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima 
compra. 
A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara 
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
'''
from os import system
from time import sleep
while True:
    system('cls')
    soma = 0
    p = 1
    print('='*50)
    print('LOJAS TABAJARA'.center(50))
    print('='*50)
    print('Registre os produtos: (digite 0 para encerrar)')
    while True:
        valor = float(input(f' - Produto {p}: R$ '))
        p += 1
        soma += valor
        if valor == 0:
            break
    print(f'\033[31mTotal: R$ {soma:.2f}\033[m')
    print('-'*50)
    forma = str(input('Qual a forma de pagamaneto?\n[ A ] - Dinheiro\n[ B ] - Cartão Débito\n[ C ] - Cartão de Crédito\n>>> ')).strip().upper()[0]
    if forma in "A":
        dinheiro = float(input('Dinheiro: R$ '))
        print(f'Troco:   R$ {dinheiro - soma:.2f}')
    elif forma in "B":
        debito = int(input('Cartão de Débito:\nDigite a senha: '))
        print('AGUARDE...')
        print('-'*50)
        sleep(1.5)
        print('TRANSAÇÃO APROVADA')
    elif forma in "C":
        print('Cartao de Crédito:')
        parc = str(input('Deseja parcelar? [S/N]: ')).strip().upper()[0]
        if parc in "S":
            print('-'*50)
            vezes = int(input('Quantas parcelas?\n2X - SEM JUROS\n3X OU MAIS 5% DE ACRESCIMO\n>>'))
            print('-'*50)
            senha = int(input('Digite a senha: '))
            print('AGUARDE...')
            print('-'*50)
            sleep(1.5)
            print('TRANSAÇÃO APROVADA')
            if vezes > 2:
                print(f'{vezes}X parcelas de R$ {(soma + (soma * 5 /100)) / vezes:.2f}')
                print(f'Total C/ JUROS R$ {soma + (soma * 5 /100):.2f}')
            elif vezes == 2:
                print(f'{vezes}X parcelas de R$ {soma / vezes:.2f}')
                print(f'Total S/ JUROS R$ {soma:.2f}')
        elif parc in "N":
            senha = int(input('Digite a senha: '))
            print('AGUARDE...')
            print('-'*50)
            sleep(1.5)
            print('TRANSAÇÃO APROVADA')
    print('OBRIGADO!! TENHA UM BOM DIA!')
    cont = str(input('>>>> DESEJA CONTINUAR? <<<<\n[S/N] ')).strip().upper()[0]
    if cont in "N":
        break
print('>>>> FIM DO PROGRAMA <<<<')



