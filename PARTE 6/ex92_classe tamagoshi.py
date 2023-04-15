''''
Credito : https://wiki.python.org.br/ExerciciosClasses ref: Ex7

Classe Bichinho Virtual:Crie uma classe que modele um Tamagoshi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade
Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade 
Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagoshi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.

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
    
    def alterarNome(self,novo_nome):
        self.nome = novo_nome

    