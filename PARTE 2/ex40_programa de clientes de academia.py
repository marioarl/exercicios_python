'''
Credito : https://wiki.python.org.br/EstruturaDeRepeticao Ex37

Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
Ao encerrar, o programa também deve informar os códigos e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
'''
from os import system
alto = baixo = mPesado = leve = 0
mediaAlt = somaAlt = mediaPesos = somaPeso = cont = 0
codAlto = codBaixo = codMpesado = codLeve= 0
while True:
    system('cls')
    print('=-'*30)
    print('ACADEMIA VAMO MALHA'.center(60))
    print('=-'*30)
    codigo = int(input('Digite seu código: (Somente numeros)' ))
    if codigo == 0:
        break
    alt = float(input('Altura........(m): '))
    somaAlt += alt
    if cont == 0:
        alto = baixo = alt
        codAlto = codBaixo = codigo
    else:
        if alt > alto:
            alto = alt
            codAlto = codigo
        elif alt < baixo:
            baixo = alt
            codBaixo = codigo

    peso = float(input('Peso.........(Kg): '))
    somaPeso += peso
    if cont == 0:
        mPesado = leve = peso
        codMpesado = codLeve = codigo
    else:
        if peso > mPesado:
            mPesado = peso
            codMpesado = codigo
        elif peso < leve:
            leve = peso
            codLeve = codigo
    cont += 1
system('cls')
mediaAlt = somaAlt / cont
mediaPesos = somaPeso / cont
print('='*60)
print('RESUMO DOS CLIENTES'.center(60))
print('='*60)
print(f' - Mais alto    >> cod: {codAlto} altura: {alto:.2f}m')
print(f' - Mais baixo   >> cod: {codBaixo} altura: {baixo:.2f}m')
print(f' - Mais pesado  >> cod: {codMpesado} peso: {mPesado:.2f}Kg')
print(f' - Menos Pesado >> cod: {codLeve} peso: {leve:.2f}Kg')
print(f'Media de altura:  {mediaAlt:.2f}m')
print(f'media de peso  :  {mediaPesos:.2f}Kg')
print('-'*28, 'FIM', '-'*28)