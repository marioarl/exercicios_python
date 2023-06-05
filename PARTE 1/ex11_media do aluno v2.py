'''
Credito : https://wiki.python.org.br/EstruturaDeDecisao Ex5
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a 7;
A mensagem "Reprovado", se a média for menor do que 7;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota:  '))
media = (n1+n2) / 2
print(f'A média das notas acima é: {media:.1f}')
print('O aluno está ', end="")
if media == 10:
    print('APROVADO COM DISTINÇÃO')
elif media >= 7:
    print('APROVADO')
else:
    print('REPROVADO')