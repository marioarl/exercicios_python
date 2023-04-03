'''
Credito : https://wiki.python.org.br/ExerciciosListas ref: Ex listas 22

Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza;
necessita troca do cabo ou conector;
quebrado ou inutilizado
Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%

'''
from os import system
from collections import Counter
from colorama import Fore, init
init(autoreset=True)

system('cls')
sit = []
desc = ['Necessita da esfera', 'Necessita de limpeza', 'Necessita troca de cabo ou conector', 'Quebrado ou inutilizado']


while True:
    print('===== SITUAÇÃO DOS MOUSES =====')
    print(Fore.YELLOW + '[ 1 ] Necessita da esfera\n[ 2 ] Necessita limpeza\n[ 3 ] Necessita troca de cabo ou conector\n[ 4 ] Quebrado ou inutilizado')
    while True:
        defeito = int(input('>>>>Opção (0 ENCERRA) ==>  '))
        if defeito >=0 and defeito <=4:
            break
    if defeito == 0:
        break
    sit.append(defeito)
    system('cls')

print(f'Quantidade de mouses: {len(sit)}')

final = Counter(sit)
print(f'{"Situação":<39}{"Qtd":>4}{"%":>10}')
for m, q in final.items():
    print(f'{m} - {desc[m-1]:<35}{q:>4}{(q/len(sit)) * 100:>10.0f}%')

