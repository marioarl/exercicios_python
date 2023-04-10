'''
Credito : https://wiki.python.org.br/ExerciciosClasses ref: Ex1

Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
'''
from os import system
class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def troca_cor(self, nova_cor):
        self.cor = nova_cor
    
    def mostra_cor(self):
        print("A cor da bola é:", self.cor)

b1 = Bola("vermelha", 50, "aço")
b1.mostra_cor()
b1.troca_cor("Azul")
b1.mostra_cor()