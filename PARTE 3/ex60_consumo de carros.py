'''
Credito : https://wiki.python.org.br/ExerciciosListas ref: Ex listas 21

Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
O modelo do carro mais econômico;
Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. A disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.
Comparativo de Consumo de Combustível

Veículo 1
Nome: fusca
Km por litro: 7
Veículo 2
Nome: gol
Km por litro: 10
Veículo 3
Nome: uno
Km por litro: 12.5
Veículo 4
Nome: Vectra
Km por litro: 9
Veículo 5
Nome: Peugeout
Km por litro: 14.5

Relatório Final
1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
2 - gol             -   10.0 -  100.0 litros - R$ 225.00
3 - uno             -   12.5 -   80.0 litros - R$ 180.00
4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
O menor consumo é do peugeout.

'''

from os import system

system('cls')
gas = float(input('Digite o preço do combustivel: R$'))
modelos =['Fusca', 'Gol', 'Uno', 'Vectra', 'Peugeout' ]
consumo = [7,10,12.5,9,14.5]
menorQtdComb = 0
modelo_menor_qtd = ""
for i in range(len(modelos)):
    print(f'Veiculo{i+1}\nNome:{modelos[i]}\nKm por litro: {consumo[i]}')

print('\nRelatório final')
print('===============')
print(f'\n{"No.":<5}{"Modelo":<10}{"Consumo":<10}{"Quantidade":<15}{"Total"}')
print(f'{"para 1000Km":>36}{"para 1000Km":>15}')
print(f'{"---":<5}{"------":<10}{"-------":<10}{"-----------":<15}{"---------"}')
for i in range(len(modelos)):
    print(f'{i+1:<5}{modelos[i]:<10} {consumo[i]:>6}{1000 / consumo[i]:>8.1f} litros  R$ {1000 / consumo[i] * gas:.2f}')
    if i == 0:
        menorQtdComb = 1000 / consumo[i]
        modelo_menor_qtd = modelos[i]
    else:
        if 1000 / consumo[i] < menorQtdComb:
            modelo_menor_qtd = modelos[i]

print(f'O menor consumo é do {modelo_menor_qtd}')
