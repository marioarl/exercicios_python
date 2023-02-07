'''
Credito : https://wiki.python.org.br/EstruturaSequencial
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido
e continue pedindo até que o usuário informe um valor válido.
'''

while True:
    nota = int(input('Digite uma nota entre 0 e 10: '))
    if nota <0 or nota >10:
        print('Valor Invalido!! ', end="")
    
    if nota >0 and nota <=10:
        break
print(f'A nota digitada foi {nota}')