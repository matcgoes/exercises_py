# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

numeros = []
pares = []
impares = []
for i in range(1,21):
    print("Numero ",i)
    numeros.append(int(input("Qual numero: ")))

for indice in range(0,len(numeros)):
    if numeros[indice]%2==0:
        pares.append(numeros[indice])
    else:
        impares.append(numeros[indice])

print("Numeros Gerais:",numeros)
print("Numeros Pares:",pares)
print("Numeros Impares:",impares)



