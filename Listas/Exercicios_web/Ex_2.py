# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []
for i in range(1,5):
    notas.append(float(input("\tNota "+str(i)+": ")))

print("Notas......")
for valores in notas:
    print(valores)

print("A média é de: ",sum(notas)/len(notas))


