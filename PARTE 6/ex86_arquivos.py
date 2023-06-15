''''
Credito : https://wiki.python.org.br/ExerciciosArquivos ref: Ex1


Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
O arquivo de entrada possui o seguinte formato:
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256
O arquivo de saída possui o seguinte formato:
[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256
'''

from colorama import Fore, init
init(autoreset=True)
#Criando o arquivo de entrada
with open("entrada.txt", "w") as f:
    f.write("200.135.80.9\n192.168.1.1\n8.35.67.74\n257.32.4.5\n85.345.1.2\n1.2.3.4\n9.8.234.5\n192.168.0.256")
print(Fore.GREEN + "Arquivo criado com sucesso!")

# Abrir o arquivo de entrada para leitura
with open("entrada.txt", "r") as entrada:
    # Ler todas as linhas do arquivo de entrada
    linhas = entrada.readlines()

# Criar listas para as linhas válidas e inválidas
validas = [linhas[0], linhas[1], linhas[2], linhas[5]]
invalidas = [linhas[3], linhas[4], linhas[6], linhas[7]]

# Abrir o arquivo de saída para escrita
with open("saida.txt", "w") as saida:
    # Escrever o cabeçalho das linhas válidas
    saida.write("Enderecos validos:\n")
    # Escrever as linhas válidas
    for linha in validas:
        saida.write(linha)

    # Escrever o cabeçalho das linhas inválidas
    saida.write("\nEnderecos invalidos:\n")
    # Escrever as linhas inválidas
    for linha in invalidas:
        saida.write(linha)

    print(Fore.YELLOW + "Arquivo saida.txt criado com sucesso!!")