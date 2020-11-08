# Faça um programa que receba dois números inteiros
# e gere os números inteiros que estão no intervalo compreendido por eles.

numero_1=int(input("Numero 1: "))
numero_2=int(input("Numero 2: "))
while numero_1 <= numero_2:
    print(numero_1)
    numero_1=numero_1+1

numero_1=int(input("Numero 1: "))
numero_2=int(input("Numero 2: "))
for i in range(numero_1,numero_2+1):
    print(numero_1)
    numero_1=numero_1+1
