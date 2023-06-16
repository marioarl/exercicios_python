''''
Crie um jogo de 21 dentro de uma função
'''

import random
def jogo_21():
    print("Bem-vindo ao jogo de 21!\n")
    while True:
        baralho = list(range(1, 11)) * 4
        random.shuffle(baralho)

        jogador = []
        dealer = []

        for i in range(2):
            jogador.append(baralho.pop())
            dealer.append(baralho.pop())

        while True:
            print(f"Suas cartas: {jogador}. Total: {sum(jogador)}")
            print(f"Carta do dealer: {dealer[0]}\n")
            opcao = input("Deseja pedir mais uma carta (s/n)? ")

            if opcao.lower() == "s":
                jogador.append(baralho.pop())

                if sum(jogador) > 21:
                    print(f"\nSuas cartas: {jogador}. Total: {sum(jogador)}")
                    print("Você ultrapassou 21! Você perdeu.")
                    return

            elif opcao.lower() == "n":
                break

        while sum(dealer) < 17:
            dealer.append(baralho.pop())

        print(f"\nSuas cartas: {jogador}. Total: {sum(jogador)}")
        print(f"Cartas do dealer: {dealer}. Total: {sum(dealer)}\n")

        if sum(dealer) > 21:
            print("O dealer ultrapassou 21! Você ganhou.")
        elif sum(jogador) > sum(dealer):
            print("Você ganhou!")
        elif sum(jogador) == sum(dealer):
            print("Empate!")
        else:
            print("Você perdeu!")
        
        nova_partida = input("\nDeseja jogar novamente (s/n)? ")
        if nova_partida.lower() == "n":
            break
            
    print("\nObrigado por jogar!")

jogo_21()

