# Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
# encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
# Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

notas = []
notas_acima = []
notas_abaixo =[]
valor=0
while valor != -1.0:
    valor=(float(input("Insira a nota: ")))
    notas.append(valor)
print("\tQuantidade de valores lidos: ",len(notas))
print("\tNotas: ",notas)
for index in reversed(range(0,len(notas))):
    print("\tNota",index+1, notas[index])
print("\tSoma dos valores: ", sum(notas))
print("\tMedia dos valores: ", sum(notas)/len(notas))
for index in range(0,len(notas)):
    if notas[index] > (sum(notas)/len(notas)):
        notas_acima.append(notas[index])
    elif notas[index] < 7:
        notas_abaixo.append(notas[index])
print("\tQuantidade de valores acima da media: ",len(notas_acima))
print("\tNotas acima da media: ", notas_acima)
print("\tQuantidade de valores abaixo de 7: ",len(notas_abaixo))
print("\tNotas abaixo de 7: ", notas_abaixo)
print("---------FIM DO PROGRAMA---------")
