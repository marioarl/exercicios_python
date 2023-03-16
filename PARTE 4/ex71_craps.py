'''
Credito : https://wiki.python.org.br/EstruturaSequencial ref: Ex funcoes 10

Jogo de Craps(ADAPTADO). Faça um programa de implemente um jogo de Craps. 
O jogador lança um par de dados, obtendo um valor entre 2 e 12.
As rodadas do Craps dão divididas em 2 seções: LANÇAMENTO DE SAIDA e PONTO.
Se, na primeira jogada, você tirar 7 ou 11, isto é um "NATURAL" e ganhou, mas se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "CRAPS" e você perdeu e termina a partida.
Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "PONTO". 
Seu objetivo agora é continuar jogando e escolhendo P(ponto) ou N(Natural) e jogando os dados até que seu saldo fique zerado ou tire CRAPS!!

'''
#NÃO TERMINADO
from os import system
from random import randint
from colorama import Fore, init
init(autoreset=True)
system('cls')

def dados():
    dado = randint(1,6)
    return dado


valor = float(input('Com qual valor voce quer entrar na mesa? R$ '))
saldo = valor

while True:
    jogTipo = ""
    dado1 = dados()
    dado2 = dados()
    total = dado1 + dado2
    print(Fore.YELLOW + '========== JOGO DE CRAPS ==========')
    print(f'{Fore.GREEN}Saldo R$: {saldo:.2f}')
    while True:
        aposta = float(input('>>>Qual sua aposta? R$ '))
        if aposta <= saldo:
            break
        print(Fore.RED + 'VALOR APOSTADO ACIMA DO SEU SALDO')
    while True:
        tipo = str(input('[P] - Ponto\n[N] - Natural\n>>> ')).strip().upper()
        if tipo in "PN":
            break
        print('Escolha P ou N!')

    print(dado1)
    print(dado2)
    if total == 7 or total == 11:
        jogTipo = "N"
        print('NATURAL!!!!!')
        if jogTipo == tipo:
            saldo += aposta + (aposta * 50 /100)      
        else:
            saldo -= aposta
    elif total >=4 and total <=8 or total >=9 and total <=10:
        jogTipo = "P"
        print('PONTO!!!!!')
        if jogTipo == tipo:
            saldo += aposta + (aposta * 10 /100)        
        else:
            saldo -= aposta 
    else:
        print('CRAPS!!!! FIM DO JOGO')

    input('Pressione enter para continuar')
    system('cls')
    if total == 2 or total == 3 or total == 12 or saldo <= 0:
        print(f'SALDO FINAL: R$ {saldo:.2f}')
        break

