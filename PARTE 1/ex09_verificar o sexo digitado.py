'''
Credito : https://wiki.python.org.br/EstruturaSequencial
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''
sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
if sexo in "M":
    print(f'Voce digitou o sexo Masculino')
elif sexo in "F":
    print(f'Voce digitou o sexo Feminino')
else:
    print('Sexo Inválido')