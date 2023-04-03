'''
Credito : https://wiki.python.org.br/ExerciciosFuncoes ref: Ex funcoes 5

Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
'''
from os import system
system('cls')

def somaImposto(taxaImposto, custo):
    imposto = custo * (taxaImposto/100)
    valor_final = custo + imposto
    return valor_final


preco = float(input('Qual o valor do produto? R$ '))
imposto = float(input('Porcentagem do imposto: '))
print(f'O valor final do produto com imposto é R$ {somaImposto(imposto,preco):.2f}')
