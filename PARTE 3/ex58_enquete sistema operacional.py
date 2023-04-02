'''
Credito : https://wiki.python.org.br/ExerciciosListas ref: Ex listas 18

Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

'''
from os import system
from collections import Counter
from colorama import Fore, init
init(autoreset=True)
def percentual(votos, total):
    r = (votos / total) * 100
    return r

def somaVotos(num):
    v = numeros.count(num)
    return v

system('cls')

numeros = []
sistema = ['Windows Server', 'Unix', 'Linux', 'NetWare', 'MacOs', 'Outro']


while True:
    print('Qual o melhor Sistema Operacional para uso em servidores?')
    print('[ 1 ] - WINDOWS SERVER\n[ 2 ] - UNIX\n[ 3 ] - LINUX\n[ 4 ] - NETWARE\n[ 5 ] - MACOS\n[ 6 ] - OUTRO')
    escolha = int(input('Escolha a sua opção: '))
    while escolha <0 or escolha > 6:
        print('Opção inválida, escolha uma das opcoes acima')
        escolha = int(input('Escolha a sua opção: '))
    if escolha == 0:
        break
    numeros.append(escolha)
    system('cls')


total = len(numeros)
system('cls')

#Variaveis para definir o vencedor, utilizando a classe Counter da biblioteca Collections
contador = Counter(numeros)
vencedor = contador.most_common(1)
votoVenc = vencedor[0][1]

print('======== RESULTADO DA ENQUETE ========')
print(f'{"Sistema operacional":<25}{"Votos":<8}{"%:":<2}')
print(f'{"-------------------":<25}{"-----":<8}{"---":<2}')
for r in range(0,6):
    #Imprimirá em vermelho se o sistema operacional for o vencedor
    if vencedor[0][0]-1 == r:
        print(Fore.RED + f'{sistema[r]:<25}{somaVotos(r+1):<8}{percentual(somaVotos(r+1), total):.1f}%')    
    else:
        print(f'{sistema[r]:<25}{somaVotos(r+1):<8}{percentual(somaVotos(r+1), total):.1f}%')


print(f'O Sistema Operacional mais votado foi o {sistema[vencedor[0][0]-1]}, com {votoVenc} votos, correspondendo a {percentual(votoVenc,total):.1f}% dos votos.')


