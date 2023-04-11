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