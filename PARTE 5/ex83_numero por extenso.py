'''
Credito : https://wiki.python.org.br/EstruturaSequencial ref: Ex Com Strings 10

Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.
'''
from os import system
system('cls')

def por_extenso(num):
    unidades = ['Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove']
    dezenas_ate_dezenove = ['Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove']
    dezenas = ['Zero', 'Dez', 'Vinte', 'Trinta', 'Quarenta', 'Cinquenta', 'Sessenta', 'Setenta', 'Oitenta', 'Noventa']

    if num == 0:
        return unidades[0]
    if num < 10:
        return unidades[num]
    if num < 20:
        return dezenas_ate_dezenove[num - 10]
    if num < 100:
        dezena = num // 10
        unidade = num % 10
        if unidade == 0:
            return dezenas[dezena]
        else:
            return dezenas[dezena] + ' e ' + unidade[unidade]
    return 'Numero fora do intervalo de 0 a 99'

numero = int(input('Digite um numero entre 0 e 99: '))
print(por_extenso(numero))
