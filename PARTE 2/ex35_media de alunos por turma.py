'''
Credito : https://wiki.python.org.br/EstruturaSequencial
Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a 
quantidade de alunos para cada turma. 
As turmas não podem ter mais de 40 alunos.
'''
media = somaQtd = 0
qtdTurmas = int(input('Qual a quantidade de turmas? '))

for t in range(1, qtdTurmas+1):
    while True:
        qtdAlunos = int(input(f'  - Quantidade de alunos da TURMA {t}: '))
        if qtdAlunos <=40:
            break
        print(f'\033[31mA turma {t} não pode ter mais de 40 alunos!\033[m')
    somaQtd += qtdAlunos
print(f'Numero médio de alunos por turma:  {somaQtd/ qtdTurmas:.1f}')
