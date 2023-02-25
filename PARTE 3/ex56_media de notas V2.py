'''
Credito : https://wiki.python.org.br/EstruturaSequencial ref: Ex listas 14

Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;

'''
from os import system
from random import randrange
from colorama import Fore, init, Style
init(autoreset=True)
system('cls')
notas = []
acimaMedida = abaixode7 = 0


while True:
    n = float(input('Digite a nota: '))
    if n == -1:
        break
    notas.append(n)
media = sum(notas) / len(notas)
#RESPONSIVIDADE DA BARRA RESUMO
tam = ((len(notas)*4) + 24) / 2
tamanho = int(tam)

print(Style.BRIGHT + Fore.YELLOW + '='*tamanho + ' RESUMO ' + '='*tamanho)
print(f'Foram digitadas {len(notas)} notas')
print(f'As notas digitas foram........: ', end="")
for n in notas:
    print(f'{n} ', end="")
print(f'\nAs notas digitas de tras para frente:')
for n in notas[::-1]:
    print(n)
print(f'Soma dos valores digitados....: {sum(notas)}')
print(f'Media dos valores.............: {media:.2f}')
for n in notas:
    if n > media:
        acimaMedida += 1
    elif n < 7:
        abaixode7 += 1
print(f'Qtd de valores acima da média: {acimaMedida}')
print(f'Qtd de valores abaixo de 7...: {abaixode7}')

