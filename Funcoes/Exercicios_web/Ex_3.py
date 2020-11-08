# Faça um programa para imprimir o triangulo de Pascal até uma linha N:
#     1
#     1   1
#     1   2   1
#     1   3   3   1
#     1   4   6   4    1
#     .......
# para um n informado pelo usuário.
#
# *vamos ter que sempre guardar o vetor anterior, mirar o mesmo elemento e somá-lo com o anterior.
# *Se for o primeiro elemento criado é 1, se for o ultimo, é 1*

def PascalTriangle():
   list=[[1], [1,1]]




def trianguloPascal(n):
    lista = [[1], [1, 1]]
    for i in range(1, n):
        linha = [1]
        for j in range(0, len(lista[i]) - 1):
            linha += [lista[i][j] + lista[i][j + 1]]
        linha += [1]
        lista += [linha]
    return lista

n = int(input("Digite o número de linhas para o triângulo de Pascal: "))
resultado = trianguloPascal(n)

for i in range(len(resultado)):
    print(resultado[i])

# a = [[1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5]]
# print(a[1][2]) = 3