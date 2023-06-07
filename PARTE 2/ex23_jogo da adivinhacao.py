'''
Jogo de adivinhação de um numero de 0 até 100, com uma variavel hint que diz se está quente ou frio o numero.
Essa variavel hint é aleatoria de 1 até 5, em cada partida ela muda de numero
'''

from random import randint
from os import system
from time import sleep

comp = randint(0,100)
cont = 0
hint = randint(1,5)
print('-='*20)
print('JOGO DA ADIVINHAÇÃO'.center(40))
print('-='*20)
print('Estou pensando em um numero de 0 a 100...')
print('Voce pode adivinhar qual é?')


while True:
      
    jog = int(input('Qual o seu palpite? \n>>>'))
    if jog > comp:
        print('Não... é  MENOR, tente novamente!')
        if jog - comp == hint:
            print('ESTÁ QUENTE!!!')
        sleep(1.5)
    elif jog < comp:
        if comp - jog == hint:
            print('ESTÁ QUENTE!!!')
        print('Não... é MAIOR, tente novamente!')
        sleep(1.5)
    cont += 1
    if comp == jog:
        print('VOCE ACERTOU!!!')
        sleep(1.5)
        break
    system('CLS')
print(f'Tentativas: {cont}')