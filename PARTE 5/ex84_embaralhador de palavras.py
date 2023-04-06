'''
Credito : https://wiki.python.org.br/ExerciciosComStrings ref: Ex Com Strings 13

Jogo da palavra embaralhada. 
Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.
'''
from os import system
from random import shuffle, randint
from time import sleep
from colorama import Fore, init
init(autoreset=True)
system('cls')

def escolher_palavra():
    with open('palavras.txt', 'r') as f:
        linhas = f.readlines()
    indice = randint(0,len(linhas) -1)
    linha = linhas[indice]
    palavra = linha.strip()
    return palavra

def embaralha(palavra):
    lista_letras = list(palavra)
    shuffle(lista_letras)
    palavra_embaralhada = " ".join(lista_letras)
    return palavra_embaralhada

escolhida = escolher_palavra()
embaralhada = embaralha(escolhida)
tentativas = 6
acertou = 0

while True:
    print(Fore.YELLOW + '##### DESCUBRA A PALAVRA EMBARALHADA #####')
    print(f'\nA PALAVRA É : {embaralhada}')
    print(f'TENTATIVAS {Fore.GREEN}{tentativas}')
    jogador = str(input('\n\nDigite a palavra: ')).strip().upper()
    acertou += 1
    if jogador == escolhida:
        print(f'ACERTOU COM {acertou} ', end="")
        print('tentativa'if acertou==1 else 'tentativas')
        if tentativas == 1:
            print(Fore.RED + 'VOCE NÃO ACERTOU!!!')
            print(f'A palavra era: {Fore.CYAN}{escolhida}')    
        break
    print(Fore.RED + 'ERRADO!! Tente novamente!')
    tentativas -= 1
    sleep(2)
    system('cls')
    