# Faça um programa para imprimir:
#     1
#     2   2
#     3   3   3
#     .....
#     n   n   n   n   n   n  ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

def ImprimeN():
    n = int(input("N? "))
    for i in range(1,n+1):
        lista =[]
        print()
        for j in range(1,i+1):
            lista.append(i)
        for index in range(0,len(lista)):
            print(lista[index],end=" ")

ImprimeN()