'''
Credito : https://wiki.python.org.br/EstruturaSequencial

Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
'''
from os import system
totAlunos = maior = menor = somaNotas = 0
nomeMaior = nomeMenor = ""

while True:
    system('cls')
    ponto = 0
    print('='*40)
    print('COLÉGIO PAGUEI PASSEI'.center(40))
    print('='*40)
    aluno = str(input('Nome do aluno: ')).strip()
    totAlunos += 1
    system('cls')
    perguntas = [{'Quantos fusos horários existem na Rússia?': 'A) 11\nB) 4\nC) 8\nD) 9\nE) 15'}, {'Qual é a flor nacional do Japão?': 'A) Flor de laranjeira\nB) Flor de cerejeira\nC) Flor de Lotus\nD) Crisantemo\nE) Flor de baunilha'}, {'Quantas tiras há na bandeira dos Estados Unidos?': 'A) 15\nB) 10\nC) 13\nD) 8\nE) 12'}, {'Qual é o animal nacional da Austrália?': 'A) Coala\nB) Tigre\nC) Tucano\nD) Canguru vermelho\nE) Leão'}, {'Quantos dias são necessários para a Terra orbitar o sol?': 'A) 360\nB) 280\nC) 300\nD) 180\nE) 365'}, {' Qual dos impérios abaixo não possui um idioma escrito': 'A) Maia\nB) Azteca\nC) Egipcio\nD) Romano\nE) Inca'}, {'Até 1923, como era chamada a cidade turca de Istambul?': 'A) Éfeso\nB) Petra\nC) Memphis\nD) Constantinopla\nE) Taxila'}, {'Qual o nome do líder da Coreia do Norte?':'A) Pak Pong-ju\nB) Kim Jong-II\nC) Kim Jong-un\nD) Moon Jae-in\nE) Xi Jinping'}, {'Quantos anos a Rainha Elizabeth II tinha quando assumiu o trono e durante quantos anos governou?':'A) 21 e 96 anos\nB) 25 e 70 anos\nC) 25 e 75 anos\nD) 20 e 70 anos\nE) 26 e 90 anos'}, {'Que país sediará as Olimpíadas de 2024?':'A) França\nB) Catar\nC) Estados Unidos\nD) Austrália\nE) Russia'}]
    for p in range(0, 10):
        print('='*40)
        print('COLÉGIO PAGUEI PASSEI'.center(40))
        print('='*40)
        print('-'*13, f'PROVA DO ALUNO {aluno}', '-'*13)
        for k,v in perguntas[p].items():
            print(f'{p+1}.{k}\n{v}')
        while True:
            try:
                res = str(input(f'Resposta: ')).strip().upper()[0]
                if res in "ABCDE":
                    break
                print('\033[31mERRO!Escolha apenas as alternativas acima!\033[m')
            except (IndexError, NameError, ValueError):
                print('\033[31mERRO!Escolha apenas as alternativas acima!\033[m')        
        if p == 0:
            if res == "A":
                ponto += 1
        elif p == 1:
            if res == "B":
                ponto += 1
        elif p == 2:
            if res == "C":
                ponto += 1
        elif p == 3:
            if res == "D":
                ponto += 1
        elif p == 4:
            if res == "E":
                ponto += 1
        elif p == 5:
            if res == "E":
                ponto += 1
        elif p == 6:
            if res == "D":
                ponto += 1
        elif p == 7:
            if res == "C":
                ponto += 1
        elif p == 8:
            if res == "B":
                ponto += 1
        elif p == 9:
            if res == "A":
                ponto += 1
        system('cls')
    if totAlunos == 1:
        maior = menor = ponto
        nomeMaior = nomeMenor = aluno
    else:
        if ponto > maior:
            maior = ponto
            nomeMaior = aluno
        if ponto < menor:
            menor = ponto
            nomeMenor = aluno
    somaNotas += ponto 
    continua = str(input('Próximo aluno? [S/N] ')).strip().upper()[0]
    if continua in "N":
        break
system('cls')       
print('='*40)
print('RESUMO DA TURMA'.center(40))
print('='*40)
print(f'Total de alunos: {totAlunos}') 
print(f'Média das notas: {somaNotas/totAlunos:.1f}')
print(f'A maior nota foi {maior} do aluno {nomeMaior}')
print(f'A menor nota foi {menor} do aluno {nomeMenor}')
    