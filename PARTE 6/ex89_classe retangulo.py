'''
Credito : https://wiki.python.org.br/ExerciciosClasses ref: Ex3

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
'''

class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
    
    def mudarLados(self, novoLadoA, novoLadoB):
        self.ladoA = novoLadoA
        self.ladoB = novoLadoB
    
    def retornarLados(self):
        return (self.ladoA, self.ladoB)
    
    def calcularArea(self):
        return self.ladoA * self.ladoB
    
    def calcularPerimetro(self):
        return 2 * (self.ladoA + self.ladoB)

# Programa principal
tamanho_local = input("Informe as medidas do local (no formato 'Largura x Comprimento'): ")
largura, comprimento = [int(i) for i in tamanho_local.split('x')]

# Cria um objeto Retangulo com as medidas informadas pelo usuário
local = Retangulo(ladoA=largura, ladoB=comprimento)

# Calcula a quantidade de pisos e rodapés necessários
area_local = local.calcularArea()
quantidade_pisos = area_local // 0.25  # cada piso tem 0.25 m²
perimetro_local = local.calcularPerimetro()
quantidade_rodapes = perimetro_local // 0.10  # cada rodapé tem 0.10 m

# Imprime os resultados
print(f"Para o local de {largura} x {comprimento} m², serão necessários:")
print(f"{quantidade_pisos} pisos (cada um com 0.25 m²)")
print(f"{quantidade_rodapes} rodapés (cada um com 0.10 m)")
