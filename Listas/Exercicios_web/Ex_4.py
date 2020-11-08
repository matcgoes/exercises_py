# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

perguntas = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?", "Já trabalhou com a vítima?"]
respostas = []

for i in range(0,len(perguntas)):
    resp=input(perguntas[i]).upper()
    while resp != "S" and resp !="N" :
        print("Responda com \"S\" ou \"N\":")
        resp = input(perguntas[i]).upper()
    if resp == "S":
        valor = 1
    else :
        valor = 0
    respostas.append(valor)

print("Quantidade de SIM: ",sum(respostas))
print(respostas)
print(len(respostas))

if sum(respostas) == 2:
    print("Você é suspeito(a)!")
elif sum(respostas) == 3 or sum(respostas) == 4:
    print("Você é cúmplice!")
elif sum(respostas) == 5:
    print("Você é assassino!!")
else:
    print("Você é inocente!!")













