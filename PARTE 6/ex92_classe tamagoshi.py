''''
Credito : https://wiki.python.org.br/ExerciciosClasses ref: Ex7

Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
'''
import os
from os import system
if os.name == "posix":
    system("clear")
else:
    system("cls")

class Tamagoshi:
    def __init__(self, nome, fome=0, saude=100, idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.humor = self.calcular_humor()

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_fome(self, nova_fome):
        self.fome = nova_fome
        self.humor = self.calcular_humor()

    def alterar_saude(self, nova_saude):
        self.saude = nova_saude
        self.humor = self.calcular_humor()

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade
        self.humor = self.calcular_humor()

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def calcular_humor(self):
        return (self.saude + (100 - self.fome)) / 2


# Criando um Tamagoshi com nome "Tama"
tama = Tamagoshi("Tama")

# Alterando os valores de fome, saude e idade do Tamagoshi
tama.alterar_fome(80)
tama.alterar_saude(60)
tama.alterar_idade(1)

# Obtendo o nome, fome, saude, idade e humor do Tamagoshi
nome = tama.retornar_nome()
fome = tama.retornar_fome()
saude = tama.retornar_saude()
idade = tama.retornar_idade()
humor = tama.calcular_humor()

