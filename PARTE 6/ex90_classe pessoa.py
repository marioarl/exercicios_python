'''
Credito : https://wiki.python.org.br/ExerciciosClasses ref: Ex4

Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''
import os
from os import system
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.altura += 0.5
    
    def engordar(self, kg):
        self.peso += kg
    
    def emagrecer(self, kg):
        self.peso -= kg
    
    def crescer(self, cm):
        self.altura += cm


pessoa1 = Pessoa('João', 18, 70, 170)
print(pessoa1.nome, pessoa1.idade,pessoa1.peso, pessoa1.altura)
pessoa1.envelhecer()
pessoa1.engordar(5)
pessoa1.crescer(2)
print(pessoa1.nome, pessoa1.idade, pessoa1.peso, pessoa1.altura)
