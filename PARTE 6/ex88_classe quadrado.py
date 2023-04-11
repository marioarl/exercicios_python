'''
Credito : https://wiki.python.org.br/ExerciciosClasses ref: Ex2

Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''
import os
from os import system

class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def mudar_lado(self, novo_lado):
        self.lado = novo_lado
    
    def retornar_lado(self):
        return self.lado
    
    def calcular_area(self):
        return self.lado ** 2

quadrado1 = Quadrado(5)
quadrado1.mudar_lado(8)
print(quadrado1.retornar_lado())
print(quadrado1.calcular_area())