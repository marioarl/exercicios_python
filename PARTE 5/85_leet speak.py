'''
Credito : https://wiki.python.org.br/ExerciciosComStrings ref: Ex Com Strings 14

Leet speak generator. 
Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak.
'''
from os import system

system('cls')

def leetSpeak(frase):
    lista_frase = list(frase)
    for l in lista_frase:
        indice = letras.index(l)
        print(leet[indice], end="")
letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', ' ']
leet = ['4','I3','[', ')', '3', '|=', '6', '#', '1', ',_|', '>|', '1', '[v]', '/v', '0', 'P', '9', 'I2', '5', '7', '(_)', '|/', 'vv', "><", 'j', '2', ' ']

print('#==== GERADOR DE LEET SPEAK ====#')
frase = str(input('Digite uma frase: ')).upper().strip()
leetSpeak(frase)

