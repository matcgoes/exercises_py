# Encontrar números primos é uma tarefa difícil.
# Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

numero = int(input("Informe o número final: "))
contador = 2
divisao = 0
while contador < numero:
    if numero%contador == 0:
        divisao = divisao + 1
    else:
        divisao = divisao
    contador = contador + 1
if divisao  == 0 and numero != 1:
    print(str(numero)+ " é primo!")
else:
    print(str(numero) + " não é primo!")