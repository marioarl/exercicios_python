'''
Credito : https://wiki.python.org.br/EstruturaDeRepeticao Ex27
Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a 
quantidade de alunos para cada turma. 
As turmas não podem ter mais de 40 alunos.
'''

from colorama import init, Fore
init(autoreset=True)
media = somaQtd = 0
qtdTurmas = int(input('Qual a quantidade de turmas? '))

for t in range(1, qtdTurmas+1):
    while True:
        qtdAlunos = int(input(f'  - Quantidade de alunos da TURMA {t}: '))
        if qtdAlunos <=40:
            break
        print(f'{Fore.RED}A turma {t} não pode ter mais de 40 alunos!')
    somaQtd += qtdAlunos
print(f'Numero médio de alunos por turma:  {somaQtd/ qtdTurmas:.1f}')
