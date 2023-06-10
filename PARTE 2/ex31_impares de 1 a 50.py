'''
Credito : https://wiki.python.org.br/EstruturaDeRepeticao Ex9
Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50
'''

#primira opcao
for i in range(1,51,2):
    print(f'{i} ', end="")

#segunda opcao
print('\n')
for i in range(1,51):
    if i % 2 == 1:
        print(f'{i} ', end="")
    