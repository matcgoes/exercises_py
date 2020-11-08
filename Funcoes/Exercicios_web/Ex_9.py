# Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12.
# Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
# Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
# Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
# Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
# Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

import random

def jogaDados():
    num = [random.randint(1,6) for i in range(0,2)]
    print("\tDado 1: ",num[0])
    print("\tDado 2: ", num[1])
    return sum(num)

def calculaResultado(soma):
    natural = [7, 11]
    craps = [2, 3, 12]
    ponto = [4, 5, 6, 8, 9, 10]
    for i in range(0,len(natural)):
        if soma == natural[i]:
            print("\nNATURAL - VOCÊ GANHOU!")
    for j in range(0,len(craps)):
        if soma == craps[j]:
            print("\nCRAPS - VOCÊ PERDEU!")
    for k in range(0,len(ponto)):
        if soma == ponto[k]:
            print("\nVOCÊ DEVE JOGAR NOVAMENTE...")
            jog2 = jogaDados()
            while jog2 != 7 and jog2 != soma:
                jog2 = jogaDados()
            if jog2 == 7:
                print("\nVOCÊ PERDEU -",jog2)
            elif jog2 == soma:
                print("\nVOCÊ GANHOU -",jog2)


jogada=jogaDados()

resultado = calculaResultado(jogada)



# Python Program to Print Rectangle Star Pattern

# rows = int(input("Please Enter the Total Number of Rows  : "))
# columns = int(input("Please Enter the Total Number of Columns  : "))
#
# print("Rectangle Star Pattern")
# for i in range(rows):
#     for j in range(columns):
#         print('*', end = '  ')
#     print()
