'''
Faça um programa que peça um certa quantidade de notas e calcule a media do alunos.
O programa será capaz de identificar a quantidade de notas e calcular e media.
'''

print('='*40)
print('COLEGIO JÁ PASSEI'.center(40))
print('='*40)
notas = []
soma = media = 0
qtdNotas = int(input('Quantas notas tem o aluno? '))
for n in range(1, qtdNotas+1):
    nota = float(input(f'Digite a {n}a. nota: '))
    notas.append(nota)
    soma += nota 
media = soma / qtdNotas
print(f'Para as notas {notas}, a média será {media:.2f}')