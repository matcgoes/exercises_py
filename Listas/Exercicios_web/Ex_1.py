# Ex1 - Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

vetor = []
tamanho = 5
elemento = 1
while elemento <= tamanho:
    vetor.append(int(input("Digite o elemento "+ str(elemento))))
    elemento = elemento + 1

for valor in vetor:
    print("\t",valor)

# Outra forma:
# for indice in range(0,len(vetor)):
#     print("\t Elemento",indice+1, vetor[indice])



# Ex 2 - Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
vetor = []
posicao = 1
while posicao <= 10:
    vetor.append(float(input("Insira o valor "+str(posicao))))
    posicao = posicao+1

# for value in range(len(vetor)-1,-1,-1):
#     print("\tValor",value+1, vetor[value])
#
# Outra forma:

for value in reversed(range(0,(len(vetor)))):
    print("\tValor ",value+1,vetor[value])


