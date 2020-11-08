# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def digit(n):
    return len(str(n))

num = int(input("Numero: "))
length = digit(num)
print(length)
