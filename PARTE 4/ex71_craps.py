'''
Credito : https://wiki.python.org.br/EstruturaSequencial ref: Ex funcoes 10

Jogo de Craps. Faça um programa de implemente um jogo de Craps. 
O jogador lança um par de dados, obtendo um valor entre 2 e 12.
As rodadas do Craps dão divididas em 2 seções: LANÇAMENTO DE SAIDA e PONTO.
Se, na primeira jogada, você tirar 7 ou 11, isto é um "NATURAL" e ganhou, mas se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "CRAPS" e você perdeu e termina a partida.
Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "PONTO". 
Seu objetivo agora é continuar jogando os dados até tirar o PONTO, que continua a rodada ou NATURAL que finaliza a rodada.
'''
from os import system
from random import randint
system('cls')

def dados():
    dado = randint(1,6)
    return dado

while True:
    dado1 = dados()
    dado2 = dados()
    total = dado1 + dado2
    print(dado1)
    print(dado2)
    if total == 7 or total == 11:
        print('NATURAL!!!!!')
    elif total >=4 and total <=8 or total >=9 and total <=10:
        print('PONTO!!!!!') 
    else:
        print('CRAPS!!!! FIM DO JOGO')

    input('Pressione enter para continuar')
    system('cls')
    if total == 2 or total == 3 or total == 12:
        break

