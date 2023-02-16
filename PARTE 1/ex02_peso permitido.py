'''
Credito : https://wiki.python.org.br/EstruturaSequencial
Joao Papo-de -Pescador, homem de bem, comprou um computador para controlar o rendimento diario
de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento
de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$4,00 por quilo excedente.
Joao precisa que voce faça um programa que leia a variavel peso(peso dos peixes) e calcule o excesso.
Gravar na variavel excesso a quantidade de quilos alem do limite e na variavel multa o valor da multa 
que o Joao devera pagar. Imprima os dados do programa com as mensagens adequadas.
'''

print('*'*30)
print('CALCULO DE EXCESSO DE PESO'.center(30))
print('*'*30)
peso = float(input('Peso dos peixes(Kg): '))

if peso > 50:
    excesso = peso - 50
    multa = 4 * excesso
    print(f'\033[31mVoce está levando {excesso}Kg acima do peso permitido(50Kg)!\033[m')
    print(f'\033[31mVoce terá que pagar uma multa de R${multa:.2f}\033[m')
else:
    print('Voce está levando a quantidade de acordo com o peso permitido')
print('Tenha um bom dia!')