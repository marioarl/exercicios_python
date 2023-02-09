'''
Credito : https://wiki.python.org.br/EstruturaSequencial
Faça um programa que calcule o mostre a média aritmética de N notas.
'''
media = soma = cont = 0

while True:
    num = float(input('Digite a nota do aluno: '))
    soma += num
    cont += 1

    while True:
        op = str(input('Continuar? [S/N] ')).strip().upper()[0]
        if op in "SN":
            break
        print('ERRO! Digite apenas S ou N')
    if op == "N":
        break    

media = soma / cont
print(f'Voce digitou {cont} notas')
print(f'A média destas notas é: {media:.2f}')