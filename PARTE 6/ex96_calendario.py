'''
Credito: w3resource.com/python-exercices/python-basic-exercices.php Ex. 12

Escreva um programa que imprima o calendario de uma dado mes e ano
Nota: Utilize o modulo calendar

'''
import calendar
ano = int(input("Ano: "))
mes = int(input("Mes: "))
print(calendar.month(ano,mes))