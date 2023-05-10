'''
Credito: w3resource.com/python-exercices/python-basic-exercices.php Ex. 22

Escreva um programa que contenha uma função que conte um numero qualquer dentro de uma lista

'''
def contador(n,nums):
    cont = 0
    for x in nums:
        if x == n:
            cont += 1
    print(f'Total de numeros {n}: {cont}')

#Contando o numero 4
contador(4,[2,5,6,7,4,3,9,10,11,4,7])

#Contando o numero 10
contador(10,[1,5,6,7,4,10,3,9,10,11,4,7,8,7,6,12,10,8])