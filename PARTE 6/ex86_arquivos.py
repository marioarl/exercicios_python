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

    print("Arquivo saida.txt criado com sucesso!!")