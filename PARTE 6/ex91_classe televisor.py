''''
Credito : https://wiki.python.org.br/ExerciciosClasses ref: Ex6

Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
Considerando os canais abertos de TV que vao do 2 até o 13 e o volume do 0 ate 10

'''

class Televisor:
    def __init__(self):
        self.__canal = 2
        self.__volume = 0

    def mudar_canal(self, canal):
        if canal >= 2 and canal <= 13:
            self.__canal = canal
            print(f"Canal: {self.__canal}")
        else:
            print("Canal inválido!")

    def aumentar_volume(self):
        if self.__volume < 10:
            self.__volume += 1
            print(f"Volume: {self.__volume}")
        else:
            print("Volume máximo atingido!")

    def diminuir_volume(self):
        if self.__volume > 0:
            self.__volume -= 1
            print(f"Volume: {self.__volume}")
        else:
            print("Volume mínimo atingido!")


tv = Televisor()

while True:
    print("1 - Mudar de canal")
    print("2 - Aumentar volume")
    print("3 - Diminuir volume")
    print("0 - Desligar")
    opcao = input("Opção: ")

    if opcao == "1":
        canal = int(input("Canal: "))
        tv.mudar_canal(canal)
    elif opcao == "2":
        tv.aumentar_volume()
    elif opcao == "3":
        tv.diminuir_volume()
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")
