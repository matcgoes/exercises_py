# Esse exercício é referente ao Exercício 113 mencionado no seguinte vídeo:
# https://www.youtube.com/watch?v=xz2B3bfNjEk

#Reescreva a função leiaInt() do desafio 104, incluindo a possibilidade da digitacao de um
# numero invalido. Aproveite e cria tambem uma função leiaFloat() com a mesma
# funcionalidade.

def leiaInt():
    while True:
        try:
            n1 = int(input("Digite um numero inteiro: "))
        except ValueError:
            print("Por favor, digite um numero inteiro valido.")     
        except KeyboardInterrupt:
            print("\nUsuario preferiu nao informar um numero.")
            return 0
        else:
            return n1

def leiaFloat():
    while True:
        try:
            n2 = float(input("Digite um numero real: "))
        except ValueError:
            print("Por favor, digite um numero real valido.")
        except KeyboardInterrupt:
            print("\nUsuario preferiu nao informar um numero.")
            return 0
        else:
            return n2

print("O numero inteiro foi {} e o numero real foi {}.".format(leiaInt(),leiaFloat()))

# print('\033[31m'+'Isto eh vermelho'+'\033[0;0m')

