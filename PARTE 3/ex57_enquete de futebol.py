'''
Credito : https://wiki.python.org.br/EstruturaSequencial ref: Ex listas 18

Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. 
Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem Python. 
Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. 
Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:

O total de votos computados;
Os números e respectivos votos de todos os jogadores que receberam votos;
O percentual de votos de cada um destes jogadores;
O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. 

O programa deve fazer uso de arrays. 
O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. 
A função calculará o percentual e retornará o valor calculado. 
Abaixo segue uma tela de exemplo. A disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador Votos           %
9               4               50,0%
10              3               37,5%
11              1               12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.

'''
from os import system
from collections  import Counter
def percentual(votos, total):
    r = (votos / total) * 100
    return r


system('cls')
apuracao = []
while True:
    while True:
        voto = int(input('Numero do jogador (0=fim): '))
        if voto >= 0 and voto <=23:
            break
        else:
            print('informe um valor entre 1 e 23 ou 0 para sair!')

    if voto == 0:
        break
    apuracao.append(voto)
#Variaveis para definir o vencedor, utilizando a classe Counter da biblioteca Collections
contador = Counter(apuracao)
vencedor = contador.most_common(1)
numeroVenc = vencedor[0][0] 
votoVenc = vencedor[0][1]

print('Enquete: Qual foi o melhor jogador?')
print('Resultado da votacao:')
print(f'\nForam computados {len(apuracao)} votos')
print(f'\n{"Jogador":<10}{"Votos":>5}{"%":>5}')

#Colocando as informacoes em um arquivo externo
arq = 'resultados.txt'
f = open('Caminho do arquivo' + arq, 'w')
f.write(f'Enquete: Quem foi o melhor jogador?\nResultado da votacaoo:\n\nForam computados {len(apuracao)} votos\n{"Jogador":<10}{"Votos":>5}{"%":>5}\n')

for v in set(apuracao):
    print(f'{v:<10}{apuracao.count(v):>3}{percentual(apuracao.count(v),len(apuracao)):>10.2f}')
    f.write(str(f'{v:<10}{apuracao.count(v):>3}{percentual(apuracao.count(v),len(apuracao)):>10.2f}\n'))

print(f'O melhor jogador foi o numero {numeroVenc}, com {votoVenc} votos, correspondendo a {percentual(votoVenc, len(apuracao)):.2f}% do total de votos.')
f.write(str(f'O melhor jogador foi o numero {numeroVenc}, com {votoVenc} votos, correspondendo a {percentual(votoVenc, len(apuracao)):.2f}% do total de votos.'))