# Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def Imprime_nesima():
    n=int(input("N? "))
    for i in range(1,n+1):
        lista=[]
        print()
        for j in range(1,i+1):
            lista.append(j)
        for index in range(0,len(lista)):
            print(lista[index],end=" ")

Imprime_nesima()