'''
Credito : https://wiki.python.org.br/EstruturaDeDecisao Ex14
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E
'''

from colorama import Fore, init
init(autoreset=True)
n1 = float(input('Digita a 1a. nota: '))
n2 = float(input('Digita a 2a. nota: '))
media = (n1 + n2) / 2
if media >= 9:
    conceito = "A"
elif media >=7.5:
    conceito = "B"
elif media >=6:
    conceito = "C"
elif media >= 4:
    conceito = "D"
else:
    conceito = "E"

print(f'As notas do aluno foram {n1:.1f} e {n2:.1f}')
print(f'A média foi de {media:.1f} com conceito "{conceito}"')
print('O aluno está ', end="")
if conceito in "ABC":
    print(Fore.YELLOW + "APROVADO")
else:
    print(Fore.RED + "REPROVADO")
